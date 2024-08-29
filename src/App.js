import './App.css';
import Header from './Header';
import HomePage from './HomePage';
import Footer from './Footer';

function App() {
  return (
    <div className="App">
      <Header className="header" />
    <HomePage className="main" />
    <Footer className="footer"/>
    </div>
  );
}

export default App;
