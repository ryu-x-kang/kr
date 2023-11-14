
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './layouts/Layout';
import Main from './pages/Main';
import MyPage from './pages/MyPage';
import Login from './pages/Login';
import TutorSearch from './pages/TutorSearch';
import TuteeSearch from './pages/TuteeSearch';
import FreeBoard from './pages/FreeBoard';
import SignUp from './pages/SignUp';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<Main />} />
                    <Route path="main" element={<Main />} />
                    <Route path="mypage" element={<MyPage />} />
                    <Route path="login" element={<Login />} />
                    <Route path="tutorsearch" element={<TutorSearch />} />
                    <Route path="tuteesearch" element={<TuteeSearch />} />
                    <Route path="freeboard" element={<FreeBoard />} />
                    <Route path="signup" element={<SignUp />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;