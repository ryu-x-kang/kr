import React from 'react';
import './Header.css';

function Header() {
    return (
        <div className="header">
            <h1 style={{ color: '#9EE5E9' }}>TutorLink</h1>
            <nav>
                <ul>
                    <li>강민철찾기</li>
                    <li>al찾기</li>
                    <li>자유게시판</li>
                    <li>자유게시판1</li>
                    <li>자유게시판1</li>
                    <li>자유게시판2</li>
                    <li>자유게시판3</li>
                    <li>자유게판2</li>
                    <li>자유게시판2</li>
                    <li>자유게시판4</li>
                    <li>자유게시판56</li>
                    <li>자유게시판78</li>
                    <li>자유게시판9</li>
                    <li>자유게시판112</li>
                    <li>튜티찾기1111</li>
                    <li>자유게시판1123123123123123</li>
                    <li>자유게시판1123123123123</li>
                    <li>자유게판2</li>
                    <li>자유게시판1</li>

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
