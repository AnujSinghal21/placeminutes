import React, { useEffect, useState } from "react";
import Sidebar from "./Sidebar";
import "../assets/nav.css";
import BarChart from "./charts/BarChart";
import branchData from "../../public/branchwise.json";
import studentData from "../../public/students.json";

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
  const [bHiLo, setBHiLo] = useState({
    "BS-SDS": {
      highestCTC: 0,
      lowestCTC: 0,
    },
  });
  const [instStats, setInstStats] = useState({
    studentsPlaced: 0,
    averageCTC: 0,
    medianCTC: 18,
    highestCTC: 0,
    lowestCTC: 128000000,
    averageCPI: 0,
  });

  const [btData, setBtData] = useState([12, 10, 110, 8]);
  const [bsData, setBsData] = useState([18, 14, 140, 6]);

  const [chartData, setChartData] = useState({});

  function extractStats() {
    const hiLo = {
      "BS-SDS": {
        highestCTC: 0,
        lowestCTC: 0,
      },
    };

    const instData = {
      studentsPlaced: 0,
      averageCTC: 0,
      medianCTC: 18,
      highestCTC: 0,
      lowestCTC: 128000000,
      averageCPI: 0,
    };
    studentData.forEach((student) => {
      const { Branch, ctc, Profile } = student;
      if (Profile !== "PIO-PPO" && Branch[0] === "B") {
        if (!hiLo[Branch]) {
          hiLo[Branch] = {
            highestCTC: ctc,
            lowestCTC: ctc,
          };
        } else {
          hiLo[Branch].highestCTC = Math.max(hiLo[Branch].highestCTC, ctc);

          hiLo[Branch].lowestCTC = Math.min(hiLo[Branch].lowestCTC, ctc);
        }
      }
      // console.log(Branch, hiLo[Branch]);
    });
    console.log(hiLo);
    setBHiLo(hiLo);

    Object.keys(branchData).forEach((branch) => {
      instData["studentsPlaced"] += branchData[branch].placed;
      instData["averageCTC"] +=
        branchData[branch].averageCTC * branchData[branch].placed;
      instData["averageCPI"] +=
        branchData[branch].averageCPI * branchData[branch].placed;
      instData["highestCTC"] = Math.max(
        instData["highestCTC"],
        hiLo[branch].highestCTC
      );
      if (branchData[branch].placed)
        instData["lowestCTC"] = Math.min(
          instData["lowestCTC"],
          hiLo[branch].lowestCTC
        );
    });
    instData["highestCTC"] /= 100000;
    instData["lowestCTC"] /= 100000;
    instData["averageCTC"] = parseFloat(
      instData["averageCTC"] / 100000 / instData["studentsPlaced"]
    ).toFixed(1);
    instData["averageCPI"] = parseFloat(
      instData["averageCPI"] / instData["studentsPlaced"]
    ).toFixed(1);

    console.log(instData);
    setInstStats(instData);
  }

  function createBTBSChart() {}
  useEffect(() => {
    /*fetch data*/
    /*extract and set data*/
    extractStats();
  }, []);

  return (
    <>
      <div className="container-fluid d-flex m-0 p-0">
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
                    {instStats.studentsPlaced}
                  </div>
                </div>
                <div className="text fs-5 text-center mt-5">
                  Students Placed
                </div>
              </div>
              <div className="avg-ctc stat-box">
                <div className="avg-ctc-data fs-1 text-center mt-4">
                  {instStats.averageCTC}
                </div>
                <div className="avg-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Average CTC</div>
              </div>
              <div className="med-ctc stat-box">
                <div className="med-ctc-data fs-1 text-center mt-4">
                  {instStats.medianCTC}
                </div>
                <div className="med-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Median CTC</div>
              </div>
              <div className="hi-ctc stat-box">
                <div className="hi-ctc-data fs-1 text-center mt-4">
                  {instStats.highestCTC}
                </div>
                <div className="hi-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Highest CTC</div>
              </div>
              <div className="lo-ctc stat-box">
                <div className="lo-ctc-data fs-1 text-center mt-4">
                  {instStats.lowestCTC}
                </div>
                <div className="lo-ctc-data fs-6 text-center">LPA</div>
                <div className="text fs-5 text-center mt-4">Lowest CTC</div>
              </div>
              <div className="avg-cpi stat-box">
                <div className="avg-cpi-data fs-1 text-center mt-4">
                  {instStats.averageCPI}
                </div>
                <div className="avg-cpi-data fs-6 text-center">/10</div>
                <div className="text fs-5 text-center mt-4">Average CPI</div>
              </div>
            </div>
            <div className="charts d-flex w-100 mt-5">
              <div className="bt-bs chart-box">
                <BarChart />
              </div>
              <div className="cpi-ctc chart-box"></div>
            </div>
          </div>
          <div className="dept-stats" style={{ width: "100%" }}>
            <h1 className="heading mt-5">Department Wise Stats</h1>
            <div className="search-bar"></div>
            <table
              className="dept-table mt-5 mx-2 fs-5"
              style={{ width: "100%" }}
            >
              <thead>
                <tr>
                  <th>
                    <>Department</>
                  </th>
                  <th>Students Placed</th>
                  <th>Average CTC</th>
                  <th>Median CTC</th>
                  <th>Highest CTC</th>
                  <th>Lowest CTC</th>
                  <th>Average CPI</th>
                </tr>
              </thead>
              <tbody>
                {Object.keys(branchData).map((dept) => {
                  // let percentage =
                  //   (100 * dept.studentsPlaced) / dept.totalStudents;
                  // percentage = parseFloat(percentage).toFixed(1);

                  return (
                    <tr key={dept}>
                      <td>{dept}</td>
                      <td>{branchData[dept].placed}</td>
                      <td>
                        {parseFloat(
                          branchData[dept].averageCTC / 100000
                        ).toFixed(1)}
                      </td>
                      <td>
                        {parseFloat(
                          branchData[dept].medianCTC / 100000
                        ).toFixed(1)}
                      </td>
                      <td>
                        {bHiLo[dept]
                          ? parseFloat(bHiLo[dept].highestCTC / 100000).toFixed(
                              1
                            )
                          : 0}
                      </td>
                      <td>
                        {bHiLo[dept]
                          ? parseFloat(bHiLo[dept].lowestCTC / 100000).toFixed(
                              1
                            )
                          : 0}
                      </td>
                      <td>
                        {parseFloat(branchData[dept].averageCPI).toFixed(1)}
                      </td>
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
