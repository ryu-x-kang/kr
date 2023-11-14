import React from 'react';
import './Header.css';

function Header() {
    return (
        <div className="header">
            <h1 style={{ color: '#9EE5E9' }}>TutorLink</h1>
            <nav>
                <ul>
                    <li>튜터찾기</li>
                    <li>튜티찾기</li>
                    <li>자유게시판</li>
                </ul>
            </nav>
            <div className="search-bar">
                <input type="text" placeholder="검색" />
               
            </div>
            <div className="user-options">
                <a href="#">로그인</a>
                <a href="#">회원가입</a>
            </div>
        </div>
    );
}

export default Header;
