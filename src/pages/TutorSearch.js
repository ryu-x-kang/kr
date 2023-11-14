import {useState} from 'react';
function TutorSearch() {
    const [searchValue, setSearchValue] = useState('');
    const [subjectValue, setSubjectValue] = useState('');
    const [schoolValue, setSchoolValue] = useState('');

    const onClickHandler = () => {
       
        console.log('검색어:', searchValue);
        console.log('희망과목:', subjectValue);
        console.log('학교명:', schoolValue);
    };

    return (
        <div>
            <h1 style={{ color: '#9EE5E9' }}>튜터찾기</h1>
        
        <div/>

        <div>
            <h3>검색어</h3>
            <div className="search-bar">
                    <input
                        type="search"
                        name="menuName"
                        value={searchValue}
                        onChange={(e) => setSearchValue(e.target.value)}
                        placeholder="검색어를 입력해보세요"
                    />
            </div>
        </div>

        <div>
            <h3>희망지역</h3>
        </div>
            
        <div>
            <h3>희망과목</h3>
            <div className="search-bar">
                    <input
                        type="search"
                        name="subject"
                        value={subjectValue}
                        onChange={(e) => setSubjectValue(e.target.value)}
                        placeholder="희망과목 입력"
                    />
            </div>
        </div>
            
        <div>
            <h3>학교명</h3>
            <div className="search-bar">
                    <input
                        type="search"
                        name="schoolName"
                        value={schoolValue}
                        onChange={(e) => setSchoolValue(e.target.value)}
                        placeholder="학교명 입력"
                    />
            </div>
        <div>
            <h3>선생님 성별</h3>
        </div>
        
        </div>

        <div className="search-bar">
                <button
                    style={{ color: 'white', backgroundColor: '#9EE5E9' }}
                    onClick={onClickHandler}
                >
                    검색하기
                </button>
            </div>
            
        </div>
    );
}

export default TutorSearch;