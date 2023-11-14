import {useState} from 'react';

function MyPage() {
    const [nameValue, setNameValue] = useState('');
    const [birthValue, setBirthValue] = useState('');

    const onClickHandler = () => {
        // 검색 버튼 클릭 시 수행할 동작 추가
        // 이 예제에서는 검색어(searchValue)를 사용할 수 있습니다.
        // console.log('이름:', nameValue);
        // console.log('출생년도:', birthValue);
        
    };

    return(
    <div>
        <div>
            <h1>마이 페이지</h1>
            <button>관심등록리스트</button>
            <button>회원정보 수정</button>
        </div>

        <div>
            <h3>실명</h3>
            <div className="search-bar">
                    <input
                        type="search"
                        name="name"
                        value={nameValue}
                        onChange={(e) => setNameValue(e.target.value)}
                        placeholder="이름을 입력해보세요"
                    />
            </div>

            <div>
                <h3>출생년도</h3>
                <div className="search-bar">
                    <input
                        type="search"
                        name="birth"
                        value={birthValue}
                        onChange={(e) => setBirthValue(e.target.value)}
                        placeholder="ex(1997)"
                        
                    />
            </div>
            
            <div>
                <h3>성별</h3>
            </div>

            <div>
                <h3>전화번호</h3>
            </div>

            <div>
                <h3>거주지</h3>
            </div>
            
            </div>
        </div>
    </div>
    );
}

export default MyPage;