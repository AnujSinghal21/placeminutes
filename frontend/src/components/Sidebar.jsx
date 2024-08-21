import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../assets/nav.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHome,
  faLightbulb,
  faBuilding,
  faUserTie,
  faCopyright,
} from "@fortawesome/free-solid-svg-icons";

function Sidebar({ page }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activePage, setActivePage] = useState(page);

  const navigate = useNavigate();

  const handleNavClick = (page) => {
    navigate(`/${page}`);
  };

  useEffect(() => {
    setActivePage(page);
    console.log(activePage);
    const navItems = document.querySelectorAll(".nav-item");

    const activeItem = document.querySelector(`.nav-item[id="${activePage}"]`);
    if (activeItem) {
      activeItem.style.color = "#A1CA8A";
    }
  }, [activePage]);
  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };
  return (
    <>
      <div
        className="d-flex"
        style={{
          minHeight: "100vh",
        }}
      >
        <nav
          className={`sidebar ${isOpen ? "d-block" : "d-none d-md-block"}`}
          style={{
            width: "16vw",
            minHeight: "100vh",
            backgroundColor: "#474B58",
          }}
        >
          <div className="sidebar-sticky">
            <h2 className="title mt-5 mx-4" style={{ color: "white" }}>
              PlaceMinutes
            </h2>
            <ul className="nav flex-column mt-5">
              <li
                className="nav-item p-4 ps-5"
                id="home"
                onClick={() => handleNavClick("home")}
              >
                <FontAwesomeIcon icon={faHome} className="me-2" />
                Home
              </li>
              <li
                className="nav-item p-4 ps-5"
                id="insights"
                onClick={() => handleNavClick("insights")}
              >
                <FontAwesomeIcon icon={faLightbulb} className="me-2" />
                Insights
              </li>
              <li
                className="nav-item p-4 ps-5"
                id="companies"
                onClick={() => handleNavClick("companies")}
              >
                <FontAwesomeIcon icon={faBuilding} className="me-2" />
                Companies
              </li>
              <li
                className="nav-item p-4 ps-5"
                id="students"
                onClick={() => handleNavClick("students")}
              >
                <FontAwesomeIcon icon={faUserTie} className="me-2" />
                Students
              </li>
              <li
                className="nav-item p-4 ps-5"
                id="contributors"
                onClick={() => handleNavClick("contributors")}
              >
                <FontAwesomeIcon icon={faCopyright} className="me-2" />
                Contributors
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </>
  );
}

export default Sidebar;
