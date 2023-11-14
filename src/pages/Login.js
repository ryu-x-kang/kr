import './Login.css';
function Login() {
    return (
        <div className="login-container">
            <h1 className="login-header">로그인</h1>
            <div className="input-container">
                <label htmlFor="username">아이디를 입력하세요</label>
                <input type="text" id="username" placeholder="아이디" />
            </div>
            <div className="input-container">
                <label htmlFor="password">비밀번호를 입력하세요</label>
                <input type="password" id="password" placeholder="비밀번호" />
            </div>
            <button className="login-button">LOGIN</button>
            <div className="login-links">
                <a href="#">회원가입하기</a>
                <a href="#">아이디/비밀번호를 잊어버렸나요?</a>
            </div>
        </div>
    );
}

export default Login;