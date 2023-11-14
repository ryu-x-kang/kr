import {NavLink} from 'react-router-dom';

function Navbar() {
    const activeStyle = {
        backgroundColor: 'purple',
        color: 'white'
    }

    return (
        <div>
            <ul>
                <li><NavLink to="/main" style={({isActive}) => isActive? activeStyle: undefined}>메인페이지</NavLink></li>
                <li><NavLink to="/mypage" style={({isActive}) => isActive? activeStyle: undefined}>마이페이지</NavLink></li>
                <li><NavLink to="/login" style={({isActive}) => isActive? activeStyle: undefined}>로그인</NavLink></li>
                <li><NavLink to="/tutorsearch" style={({isActive}) => isActive? activeStyle: undefined}>튜터찾기</NavLink></li>
                <li><NavLink to="/tuteesearch" style={({isActive}) => isActive? activeStyle: undefined}>튜티찾기</NavLink></li>
                <li><NavLink to="/freeboard" style={({isActive}) => isActive? activeStyle: undefined}>자유게시판1</NavLink></li>
                <li><NavLink to="/signup" style={({isActive}) => isActive? activeStyle: undefined}>회원가입</NavLink></li>
            </ul>
        </div>
    );
}

export default Navbar;