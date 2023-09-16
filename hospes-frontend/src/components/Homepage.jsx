
import { motion } from "framer-motion";
import Header from "./Header";
import SearchBar from "./SearchBar";
import Loading from "./Loading";
import HomeViewContainer from "./HomeViewContainer";
import Modal from "./Modal";
const Homepage = () => {

    return (
        <>
            <Header/>
            <div className="body-container">
                <div className="main-container">
                    <div className="content">
                        <div className="title">
                            <h1 style={{fontWeight:"bolder"}}>Welcome to Hospes</h1>
                        </div>
                        <div className="subtitle">
                            <h4>Where you don't just find a home, you find a <i style={{color:"red"}}>family.</i></h4>
                        </div>
                    </div>
                    <SearchBar/>
                    <HomeViewContainer/>
                    <Loading/>
                </div>
            </div>
            <Modal/>
        </>
        
    )
}
export default Homepage;