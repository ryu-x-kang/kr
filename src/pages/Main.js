function Profile({ imageSrc, text }) {
    return (
        <div className="profile">
            <img src={imageSrc} alt="프로필 이미지" />
            <p>{text}</p>
        </div>
    );
}

function Main() {
    return (
        <div>
            <h1>튜터찾고 대학가자!</h1>
            <h1>검증된 튜터</h1>
            <div className="profiles-container">
                <Profile
                    imageSrc="url_to_image1.jpg"
                    text="서울대 경영학과"
                />
                <Profile
                    imageSrc="url_to_image2.jpg"
                    text="연세대 경영학과"
                />
                <Profile
                    imageSrc="url_to_image3.jpg"
                    text="고려대 경영학과"
                />
            <h1>튜터링크 게시판 물어보세요!</h1>
            </div>
        </div>

        
    );
}

export default Main;