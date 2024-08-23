import React, { useEffect, useState } from "react";
import Sidebar from "./Sidebar";
import "../assets/nav.css";
import studentData from "../../public/students.json";

function Students() {
  const [data, setData] = useState(
    studentData.filter((student) => {
      return student["Branch"][0] === "B";
    })
  );
  const [currentPage, setCurrentPage] = useState(1);
  const [entries, setEntries] = useState(10);
  const [currentData, setCurrentData] = useState(data.slice(0, 10));

  function handleNext() {
    setCurrentPage(currentPage + 1);
  }
  function handlePrev() {
    setCurrentPage(currentPage - 1);
  }

  function handleEntries(event) {
    setEntries(Number(event.target.value));
    setCurrentPage(1);
  }

  useEffect(() => {
    setCurrentData(data.slice(currentPage - 1, currentPage * entries));
  }, [entries, currentPage]);
  return (
    <>
      <div
        className="container-fluid d-flex m-0 p-0"
        style={{ backgroundColor: "#1c2130", height: "100vh" }}
      >
        <Sidebar page={"students"} />
        <div className="container-fluid hide-scrollbar overflow-scroll p-5">
          <h1 className="heading mb-5">Student List</h1>
          <div className="search"></div>
          <table className="std-table fs-6">
            <thead>
              <tr>
                <th>Sr. No.</th>
                <th>Name</th>
                <th>Roll No.</th>
                <th>Profile</th>
                <th>Company</th>
                <th>CTC (in LPA)</th>
                <th>Department</th>
              </tr>
            </thead>
            <tbody>
              {currentData.map((student, index) => {
                if (student["Branch"][0] !== "B") {
                  return <></>;
                }
                return (
                  <tr key={student["Roll No."]}>
                    <td>{index + 1}</td>
                    <td>{student["Name"]}</td>
                    <td>{student["Roll No."]}</td>
                    <td>{student["Profile"]}</td>
                    <td>{student["Company Name"]}</td>
                    <td>{parseFloat(student["ctc"] / 100000).toFixed(1)}</td>
                    <td>{student["Branch"]}</td>
                  </tr>
                );
              })}
            </tbody>
            <tfoot>
              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td style={{ textAlign: "right", color: "#474B58" }}>
                  Showing {currentPage} out of{" "}
                  {Math.ceil(data.length / entries)}
                </td>
                <td>
                  <button
                    disabled={currentPage === 1 ? true : false}
                    onClick={handlePrev}
                  >
                    Previous
                  </button>
                  <button
                    disabled={
                      currentPage * entries >= data.length ? true : false
                    }
                    onClick={handleNext}
                  >
                    Next
                  </button>
                </td>
                <td>
                  <label className="me-2">Show</label>
                  <select
                    name="entries"
                    id="entries"
                    value={entries}
                    onChange={handleEntries}
                    style={{ color: "#1c2130" }}
                  >
                    <option value={10}>10</option>
                    <option value={20}>20</option>
                    <option value={30}>30</option>
                    <option value={50}>50</option>
                    <option value={"All"}>All</option>
                  </select>
                </td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </>
  );
}

export default Students;
