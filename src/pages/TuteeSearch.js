// function TuteeSearch() {
//     return(
//     <div>
//       <h1>튜터 찾기</h1>
//       <h3>검색어</h3>
//     </div>
//     );
// }

// export default TuteeSearch;

// function TuteeSearch() {
//     return (
//         <div>
//             <h1 style={{ color: '#9EE5E9' }}>튜터찾기</h1>
//             <h3>검색어 </h3>
//             <h3>희망지역 </h3>
//             <h3>희망과목</h3>
//             <h3>학생성별</h3>
//             <div className="search-bar">
//                 <input type="text" placeholder="검색하기" />
//                 <button style={{ color: 'white', backgroundColor: '#9EE5E9' }}>검색</button>
//             </div>
//         </div>
//     );
// }

// export default TuteeSearch;
import {useState} from 'react';

function TuteeSearch() {
    const [searchValue, setSearchValue] = useState('');
    const [subjectValue, setSubjectValue] = useState('');
    // const [locationValue, setLocationValue] = useState('');
    

    const onClickHandler = () => {
        
        // console.log('검색어:', searchValue);
        // console.log('희망과목:', subjectValue);
        
    };

    return (
        <div>
            <h1 style={{ color: '#9EE5E9' }}>튜티찾기</h1>
        
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
            {/* <div className="search-bar">
                <input
                    type="search"
                    name="location"
                    value={locationValue}
                    onChange={(e) => setLocationValue(e.target.value)}
                    placeholder="희망지역 입력"
                />
            </div> */}
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
            <h3>학생성별</h3>
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

export default TuteeSearch;