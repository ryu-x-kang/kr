from math import ceil
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from function import error, login_required
from MySQLdb.cursors import DictCursor


import io
import base64
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "1111"
app.config["MYSQL_DB"] = "diarysys"

mysql = MySQL(app)


@app.route("/", methods=["GET"])
@login_required
def index():
    if session.get("pagenation") is None:
        session["pagenation"] = int(request.args.get("pagenation", 5))

    if request.args.get("pagenation") is not None:
        session["pagenation"] = int(request.args.get("pagenation"))

    pagenation_list = [5, 10, 15, 20]

    pagenation = session["pagenation"]
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT diary_id, diary_title, diary_cont, diary_date FROM diary WHERE user_email = %s ORDER BY diary_id DESC",
        (session["user_email"],),
    )
    diary_list = cur.fetchall()
    cur.execute(
        "SELECT announcement_id, announcement_title, announcement_cont, announcement_date FROM announcement ORDER BY announcement_id DESC"
    )
    announcement_list = cur.fetchall()
    cur.close()

    cur_page = int(request.args.get("page", 1))
    total_page = ceil(len(diary_list) / pagenation)
    pages = [page for page in range(1, total_page + 1) if abs(cur_page - page) <= 3]
    if not total_page == cur_page:
        cur_diary_list = diary_list[
            (cur_page - 1) * pagenation : (cur_page - 1) * pagenation + pagenation
        ]
    else:
        cur_diary_list = list(diary_list[(cur_page - 1) * pagenation :])

    
    return render_template(
        "index.html",
        cur_diary_list=cur_diary_list,
        cur_page=cur_page,
        pages=pages,
        pagenation_list=pagenation_list,
        announcement_list=announcement_list,
        pagenation=pagenation,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        domain = request.form.get("domain")
        email=username+'@'+domain
        password = request.form.get("password")

        cur = mysql.connection.cursor(DictCursor)
        cur.execute("SELECT * FROM user WHERE user_email = %s", (email,))
        user = cur.fetchone()
        cur.close()
        if user and check_password_hash(user["user_pwd"], password):
            session["user_email"] = email
            return redirect("/")
        else:
            return error("로그인 실패, 아이디 또는 패스워드를 확인하세요.")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        domain = request.form.get("domain")
        email=username+'@'+domain
        password = request.form.get("password")
        password_confirm = request.form.get("password-confirm")
        question_id = request.form.get("question")
        answer = request.form.get("answer")

        if password != password_confirm:
            return error("비밀번호가 일치하지 않습니다.")

        password_hash = generate_password_hash(
            password, method="pbkdf2", salt_length=16
        )

        cur = mysql.connection.cursor(DictCursor)
        cur.execute("SELECT user_email FROM user")
        users = cur.fetchall()
        if email in [user["user_email"] for user in users]:
            return error("이미 가입한 이메일입니다.")

        cur.execute(
            "INSERT INTO user (user_email, user_pwd, user_ans, question_id) VALUES (%s, %s, %s, %s)",
            (email, password_hash, answer, question_id),
        )
        mysql.connection.commit()
        cur.close()

        return redirect("/login")

    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM question")
        question_list = cur.fetchall()
        cur.close()
        return render_template("register.html", question_list=question_list)


@app.route("/change-member-info", methods=["GET"])
@login_required
def change_member_info():
    return render_template("change-member-info.html", email=session["user_email"])


@app.route("/deregister", methods=["POST"])
@login_required
def deregister():
    reason = request.form.get("reason")  # 탈퇴 사유를 가져옴

    cur = mysql.connection.cursor()
    # 사용자 정보를 why_secession 테이블에 저장
    cur.execute(
        "INSERT INTO whysecession (whysecession_cont) VALUES (%s)",
        (reason,),
    )
    # 사용자 정보를 user 테이블에서 삭제
    cur.execute(
        "DELETE FROM user WHERE user_email = %s", (session["user_email"],)
    )
    mysql.connection.commit()
    cur.close()

    # 로그아웃 후 로그인 페이지로 리디렉션
    session.clear()
    return redirect("/login")


@app.route("/email-find", methods=["GET", "POST"])
def email_find():
    if request.method == "POST":
        username = request.form.get("username")
        domain = request.form.get("domain")
        email=username+'@'+domain
        cur = mysql.connection.cursor()
        cur.execute("SELECT user_email FROM user WHERE user_email = %s;", (email,))
        user_email = cur.fetchone()
        cur.close()

        if not user_email:
            return error("입력하신 아이디가 없습니다.")

        session["tmp_email"] = email

        return redirect("/password-find")
    else:
        return render_template("email-find.html")


@app.route("/password-find", methods=["GET", "POST"])
def password_find():
    email = session["tmp_email"]

    if request.method == "POST":
        cur = mysql.connection.cursor(DictCursor)
        cur.execute("SELECT user_ans FROM user WHERE user_email = %s;", (email,))
        user_ans = cur.fetchone()
        cur.close()

        if user_ans == None:
            session.clear()
            return error("그런사람없읍니다.")
        elif user_ans["user_ans"] != request.form.get("answer"):
            session.clear()
            return error("답변이 틀렸습니다.")
        return redirect("/password-reset")
    else:
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT question_id FROM user WHERE user_email = %s;",
            (email,),
        )
        question_id = cur.fetchone()
        cur.execute(
            "SELECT question_cont FROM question WHERE question_id = %s;", (question_id,)
        )
        question_cont = cur.fetchone()
        cur.close()

        return render_template("password-find.html", question_cont=question_cont[0] )


@app.route("/password-reset", methods=["GET", "POST"])
def password_reset():
    if session.get("user_email") is None:
        email = session["tmp_email"]
    else:
        email = session["user_email"]


    if request.method == "POST":
        # db에 비밀번호 업데이트 후 재설정
        password = request.form.get("password")
        password_confirm = request.form.get("password-confirm")

        if password != password_confirm:
            return error("비밀번호가 일치하지 않습니다.")
        else:
            pwd_new = generate_password_hash(password, method="pbkdf2", salt_length=16)
            cur = mysql.connection.cursor()
            cur.execute(
                "UPDATE user SET user_pwd=%s WHERE user_email = %s",
                (pwd_new, email),
            )
            mysql.connection.commit()
            cur.close()
        session.clear()
        return redirect("/")
    else:
        return render_template("password-reset.html", email=email)


@app.route("/feeling", methods=["GET", "POST"])
@login_required
def feeling():
    if request.method == "POST":
        feeling_value = request.form.get("feeling")
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM feeling WHERE feeling_date = CURDATE() AND user_email = %s",
            (session["user_email"],),
        )

        if cur.fetchone() != None:
            cur.execute(
                "UPDATE feeling SET feeling = %s WHERE feeling_date = CURDATE() AND user_email = %s",
                (
                    feeling_value,
                    session["user_email"],
                ),
            )
        else:
            cur.execute(
                "INSERT INTO feeling (feeling_date, feeling, user_email) VALUES (NOW(), %s, %s)",
                (
                    feeling_value,
                    session["user_email"],
                ),
            )
        mysql.connection.commit()
        cur.close()
        return redirect("/feeling")
    else:
        # SQL 쿼리 실행을 위한 커서 생성
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT DATE_FORMAT(feeling_date, '%%Y%%m%%d%%H'), feeling FROM feeling WHERE user_email = %s",
            (session["user_email"],),
        )
        result = cur.fetchall()
        cur.close()

        if len(result) <= 3:
            pass
        else:
            df = pd.DataFrame(result, columns=["date", "feeling"])
            df["date"] = pd.to_datetime(df["date"], format="%Y%m%d%H")
            f = interp1d(df["date"].astype(np.int64), df["feeling"], kind="cubic")

            xnew = np.linspace(
                df["date"].astype(np.int64).min(),
                df["date"].astype(np.int64).max(),
                1000,
            )

            # 보간 함수를 사용하여 y값 생성
            ynew = f(xnew)

            # 그래프 그리기, 마커는 제거함
            plt.plot(xnew.astype("datetime64[ns]"), ynew, "-")

        plt.xlabel("date")
        plt.ylabel("feeling")
        plt.title("Feeling", fontsize=16)

        # y축 눈금과 레이블을 사용자 정의 값으로 설정
        plt.yticks([-2, -1, 0, 1, 2], ["😟", "😯", "😐", "😀", "😄"])

        # 0을 기준으로 하는 x 축 표현
        plt.axhline(0, color="black", linewidth=0.8)

        # 그래프 테두리 제거
        for spine in plt.gca().spines.values():
            spine.set_visible(False)

        plt.gcf().autofmt_xdate()

        # 그래프를 이미지 버퍼로 저장
        img = io.BytesIO()
        plt.savefig(img, format="png", bbox_inches="tight")
        plt.close()  # 열린 그래프 창을 닫습니다.
        img.seek(0)

        # 이미지를 base64 인코딩하여 HTML에 직접 표시 가능한 문자열로 변환
        plot_url = base64.b64encode(img.getvalue()).decode()

        # HTML 템플릿에 데이터를 전달
        return render_template("feeling.html", plot_url=plot_url)


@app.route("/read-post", methods=["GET"])
@login_required
def read_post():
    current_diary_id = int(request.args.get("diary_id"))

    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT diary_id, diary_title, diary_cont, diary_date FROM diary WHERE user_email = %s ORDER BY diary_id;",
        (session["user_email"],),
    )
    diary_list = cur.fetchall()
    cur.close()
    diary = {}
    prev_diary_id, next_diary_id = 0, 0

    for diary_id, diary_title, diary_cont, diary_date in diary_list:
        if diary_id < current_diary_id:
            prev_diary_id = diary_id
        elif current_diary_id < diary_id:
            next_diary_id = diary_id
            break
        else:
            diary["title"] = diary_title
            diary["cont"] = diary_cont
            diary["date"] = diary_date
    return render_template(
        "read-post.html",
        prev_diary_id=prev_diary_id,
        next_diary_id=next_diary_id,
        diary=diary,
    )

@app.route("/read-announcement", methods=["GET"])
@login_required
def read_announcement():
    current_announcement_id = int(request.args.get("announcement_id"))

    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT announcement_id, announcement_title, announcement_cont, announcement_date FROM announcement ORDER BY announcement_id"

    )
    announcement_list = cur.fetchall()
    cur.close()
    announcement = {}
    prev_announcement_id, next_announcement_id = 0, 0

    for announcement_id, announcement_title, announcement_cont, announcement_date in announcement_list:
        if announcement_id < current_announcement_id:
            prev_announcement_id = announcement_id
        elif current_announcement_id < announcement_id:
            next_announcement_id = announcement_id
            break
        else:
            announcement["title"] = announcement_title
            announcement["cont"] = announcement_cont
            announcement["date"] = announcement_date
    return render_template(
        "read-announcement.html",
        prev_announcement_id=prev_announcement_id,
        next_announcement_id=next_announcement_id,
        announcement=announcement,
    )


@app.route("/write-post", methods=["GET", "POST"])
@login_required
def write_post():
    # 글의 정보를 받아서 포스
    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO diary (diary_title, diary_cont, user_email, diary_date) VALUES (%s, %s, %s, NOW())",
            (title, content, session["user_email"]),
        )
        mysql.connection.commit()
        cur.close()

        return redirect("/")
    else:
        return render_template("write-post.html")


@app.route("/search", methods=["GET"])
@login_required
def search():
    # 글의 정보를 받아서 포스
    if session.get("term") is None:
        session["term"] = request.args.get("term")
    
    if request.args.get("term") is not None:
        session["term"] = request.args.get("term")
    
    term = session["term"]
    
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT diary_id, diary_title, diary_cont, diary_date FROM diary WHERE diary_title LIKE %s OR diary_cont LIKE %s ORDER BY diary_id",
        ("%" + term + "%", "%" + term + "%"),
    )
    diary_list = cur.fetchall()
    cur.close()

    if session.get("pagenation") is None:
        session["pagenation"] = int(request.args.get("pagenation", 5))

    if request.args.get("pagenation") is not None:
        session["pagenation"] = int(request.args.get("pagenation"))

    pagenation_list = [5, 10, 15, 20]

    pagenation = session["pagenation"]

    cur_page = int(request.args.get("page", 1))
    total_page = ceil(len(diary_list) / pagenation)
    pages = [page for page in range(1, total_page + 1) if abs(cur_page - page) <= 3]
    if not total_page == cur_page:
        cur_diary_list = diary_list[
            (cur_page - 1) * pagenation : (cur_page - 1) * pagenation + pagenation
        ]
    else:
        cur_diary_list = diary_list[(cur_page - 1) * pagenation :]

    return render_template(
        "search.html", cur_diary_list=cur_diary_list, term=term, number=len(diary_list),cur_page=cur_page,pages=pages,pagenation_list=pagenation_list,pagenation=pagenation
    )
