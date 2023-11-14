import React from 'react';
import { useParams } from 'react-router-dom';
// import PageNumber from '../components/PageNumber';

function FreeBoard() {
    const { page } = useParams();

    return (
        <div>
            <h1 style={{ color: '#9EE5E9' }}>자유게시판</h1>
            <div className="search-bar">
                <input type="text" placeholder="검색어를 입력해 보세요" />
                <button style={{ backgroundColor: '#9EE5E9' }}>검색</button>
            </div>
            <button style={{ backgroundColor: '#9EE5E9' }}>글쓰기</button>
            <table>
                <thead>
                    <tr>
                        <th>번호</th>
                        <th>제목</th>
                        <th>작성자</th>
                        <th>작성일자</th>
                        <th>첨부파일</th>
                    </tr>
                </thead>
                <tbody>
                    {/* 테이블 데이터(동적)  */}
                </tbody>
            </table>
            {/* 페이지 번호 렌더링 */}
            
            <div className="page-numbers">
                {/* <PageNumber page={page} /> */}
                {/* 페이지 번호 추가*/}
            </div>
        </div>
    );
}

export default FreeBoard;
