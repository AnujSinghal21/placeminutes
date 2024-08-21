import React from "react";
import Sidebar from "./Sidebar";

function Companies() {
  return (
    <>
      <div
        className="container-fluid flex m-0 p-0 w-100"
        style={{ backgroundColor: "#1c2130" }}
      >
        <Sidebar page={"companies"} />
        <div className="container"></div>
      </div>
    </>
  );
}

export default Companies;
