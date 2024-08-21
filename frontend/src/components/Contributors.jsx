import React from "react";
import Sidebar from "./Sidebar";

function Contributors() {
  return (
    <>
      <div
        className="container-fluid flex m-0 p-0 w-100"
        style={{ backgroundColor: "#1c2130" }}
      >
        <Sidebar page={"contributors"} />
        <div className="container"></div>
      </div>
    </>
  );
}

export default Contributors;
