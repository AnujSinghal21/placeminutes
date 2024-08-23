import React, { useState, useEffect } from "react";
import Sidebar from "./Sidebar";
import "../assets/nav.css";
import companyData from "../../public/companies.json";

function Companies() {
  const [data, setData] = useState(companyData);
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
      <div className="container-fluid d-flex m-0 p-0">
        <Sidebar page={"companies"} />
        <div
          className="container-fluid p-5 overflow-scroll hide-scrollbar"
          style={{ backgroundColor: "#1c2130" }}
        >
          <h1 className="heading mb-5">Companies List</h1>
          <table className="cmp-table fs-6">
            <thead>
              <tr>
                <th>Sr. No.</th>
                <th>Name</th>
                <th>Profile</th>
                <th>Role</th>
                <th>CTC (in LPA)</th>
                <th>Location</th>
              </tr>
            </thead>
            <tbody>
              {currentData.map((company, index) => {
                return (
                  <tr key={company["id"]}>
                    <td>{index + 1}</td>
                    <td>{company["name"]}</td>
                    <td>{company["profile"]}</td>
                    <td>{company["role"]}</td>
                    <td>{parseFloat(company["ctc"] / 100000).toFixed(1)}</td>
                    <td>{company["location"]}</td>
                  </tr>
                );
              })}
            </tbody>
            <tfoot>
              <tr>
                <td
                  style={{ textAlign: "right", color: "#474B58" }}
                  colSpan={4}
                >
                  Showing {currentPage} out of{" "}
                  {Math.ceil(data.length / entries)}
                </td>
                <td>
                  <label className="me-2">Show</label>
                  <select
                    name="entries"
                    id="entries"
                    value={entries < data.length ? String(entries) : "ALL"}
                    onChange={handleEntries}
                    style={{ color: "#1c2130" }}
                  >
                    <option value={10}>10</option>
                    <option value={20}>20</option>
                    <option value={30}>30</option>
                    <option value={50}>50</option>
                    <option value={data.length}>All</option>
                  </select>
                </td>
                <td colSpan={1}>
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
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </>
  );
}

export default Companies;
