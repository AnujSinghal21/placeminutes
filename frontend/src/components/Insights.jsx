import React from "react";
import Sidebar from "./Sidebar";

function Insights() {
  return (
    <>
      <div
        className="container-fluid flex m-0 p-0 w-100"
        style={{ backgroundColor: "#1c2130" }}
      >
        <Sidebar page={"insights"} />
        <div className="container"></div>
      </div>
    </>
  );
}

export default Insights;
