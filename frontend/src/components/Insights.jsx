import React, { useEffect, useState } from "react";
import Sidebar from "./Sidebar";
import "../assets/nav.css";

function Insights() {
  const [data, setData] = useState({
    INST: {
      studentsPlaced: 1234,
      totalStudents: 2345,
      averageCTC: 15,
      medianCTC: 12,
      highestCTC: 140,
      lowestCTC: 6,
      averageCPI: 7,
    },
    BT: {
      studentsPlaced: 600,
      totalStudents: 920,
      averageCTC: 18,
      medianCTC: 14,
      highestCTC: 140,
      lowestCTC: 6,
      averageCPI: 7,
    },
    BS: {
      studentsPlaced: 334,
      totalStudents: 542,
      averageCTC: 12,
      medianCTC: 10,
      highestCTC: 110,
      lowestCTC: 8,
      averageCPI: 6.5,
    },
    MT: {
      studentsPlaced: 320,
      totalStudents: 912,
      averageCTC: 16,
      medianCTC: 11,
      highestCTC: 80,
      lowestCTC: 8,
      averageCPI: 7,
    },
    DEPT: [
      {
        name: "CSE",
        studentsPlaced: 120,
        totalStudents: 121,
        averageCTC: 22,
        medianCTC: 20,
        highestCTC: 140,
        lowestCTC: 15,
        averageCPI: 7.5,
      },
      {
        name: "EE",
        studentsPlaced: 170,
        totalStudents: 190,
        averageCTC: 18,
        medianCTC: 15,
        highestCTC: 120,
        lowestCTC: 8,
        averageCPI: 7,
      },
      {
        name: "EE",
        studentsPlaced: 170,
        totalStudents: 190,
        averageCTC: 18,
        medianCTC: 15,
        highestCTC: 120,
        lowestCTC: 8,
        averageCPI: 7,
      },
      {
        name: "EE",
        studentsPlaced: 170,
        totalStudents: 190,
        averageCTC: 18,
        medianCTC: 15,
        highestCTC: 120,
        lowestCTC: 8,
        averageCPI: 7,
      },
      {
        name: "EE",
        studentsPlaced: 170,
        totalStudents: 190,
        averageCTC: 18,
        medianCTC: 15,
        highestCTC: 120,
        lowestCTC: 8,
        averageCPI: 7,
      },
      {
        name: "EE",
        studentsPlaced: 170,
        totalStudents: 190,
        averageCTC: 18,
        medianCTC: 15,
        highestCTC: 120,
        lowestCTC: 8,
        averageCPI: 7,
      },
    ],
  });
  const [instPerc, setInstPerc] = useState(75);

  useEffect(() => {
    /*fetch data*/
    /*extract and set data*/
    const perc = (100 * data.INST.studentsPlaced) / data.INST.totalStudents;
    setInstPerc(parseFloat(perc).toFixed(1));
  }, []);

  return (
    <>
      <div className="container-fluid d-flex m-0 p-0 w-100">
        <Sidebar page={"insights"} />
        <div
          className="container-fluid p-5 overflow-scroll hide-scrollbar"
          style={{ backgroundColor: "#1c2130", height: "100vh" }}
        >
          <div className="inst-stats">
            <h1 className="heading mb-5">Institute Stats</h1>
            <div className="w-100 d-flex">
              <div className="st-pl stat-box">
                <div className="data flex-column">
                  <div className="st-pl-data fs-1 text-center mt-4">
                    {instPerc}%
                  </div>
                  <div className="st-pl-data fs-6 text-center">
                    {data.INST.studentsPlaced}/{data.INST.totalStudents}
                  </div>
                </div>
                <div className="text fs-5 text-center mt-4">
                  Students Placed
                </div>
              </div>
              <div className="avg-ctc stat-box">
                <div className="avg-ctc-data fs-1 text-center mt-4">
                  {data.INST.averageCTC}
                </div>
                <div className="avg-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Average CTC</div>
              </div>
              <div className="med-ctc stat-box">
                <div className="med-ctc-data fs-1 text-center mt-4">
                  {data.INST.medianCTC}
                </div>
                <div className="med-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Median CTC</div>
              </div>
              <div className="hi-ctc stat-box">
                <div className="hi-ctc-data fs-1 text-center mt-4">
                  {data.INST.highestCTC}
                </div>
                <div className="hi-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Highest CTC</div>
              </div>
              <div className="lo-ctc stat-box">
                <div className="lo-ctc-data fs-1 text-center mt-4">
                  {data.INST.lowestCTC}
                </div>
                <div className="lo-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Lowest CTC</div>
              </div>
              <div className="avg-cpi stat-box">
                <div className="avg-cpi-data fs-1 text-center mt-4">
                  {data.INST.averageCPI}
                </div>
                <div className="avg-cpi-data fs-6 text-center">/10</div>
                <div className="text fs-5 text-center mt-4">Average CPI</div>
              </div>
            </div>
            <div className="charts d-flex w-100 mt-5">
              <div className="bt-bs chart-box"></div>
              <div className="cpi-ctc chart-box"></div>
            </div>
          </div>
          <div className="dept-stats" style={{ width: "100%" }}>
            <h1 className="heading mt-5">Department Wise Stats</h1>
            <div className="search-bar"></div>
            <div className="filter"></div>
            <table
              className="dept-table mt-5 mx-2 fs-5"
              style={{ width: "100%" }}
            >
              <thead>
                <tr>
                  <th>Department</th>
                  <th>Placed Percentage</th>
                  <th>Average CTC</th>
                  <th>Median CTC</th>
                  <th>Highest CTC</th>
                  <th>Lowest CTC</th>
                  <th>Average CPI</th>
                </tr>
              </thead>
              <tbody>
                {data.DEPT.map((dept) => {
                  let percentage =
                    (100 * dept.studentsPlaced) / dept.totalStudents;
                  percentage = parseFloat(percentage).toFixed(1);
                  return (
                    <tr>
                      <td>{dept.name}</td>
                      <td>{percentage}%</td>
                      <td>{dept.averageCTC}</td>
                      <td>{dept.medianCTC}</td>
                      <td>{dept.highestCTC}</td>
                      <td>{dept.lowestCTC}</td>
                      <td>{dept.averageCPI}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
}

export default Insights;
