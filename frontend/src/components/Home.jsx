import React from "react";
import Sidebar from "./Sidebar";

function Home() {
  return (
    <>
      <Sidebar page={"home"} />
      <div style={{ padding: "20px", textAlign: "center" }}>
        <h1>Welcome to the Home Page</h1>
        <p>This is the home page of your React application.</p>
        <p>Feel free to explore the other pages using the navigation links.</p>
      </div>
    </>
  );
}

export default Home;
