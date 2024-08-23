import React from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

const BarChart = ({ chartData }) => {
  const data = {
    labels: ["Average CTC", "Median CTC", "Highest CTC", "Lowest CTC"],
    datasets: [
      {
        label: "BT",
        data: [18, 14, 140, 6], // Example data for BTech
        backgroundColor: "#028F76",
        borderColor: "#028F76",
        borderWidth: 1,
      },
      {
        label: "BS",
        data: [12, 10, 110, 8], // Example data for BS
        backgroundColor: "#FFEAAD",
        borderColor: "#FFEAAD",
        borderWidth: 1,
      },
    ],
  };

  const options = {
    indexAxis: "y", // This makes the bar chart horizontal
    scales: {
      x: {
        beginAtZero: true,
        ticks: {
          color: "#FFFFFF", // Color for x-axis labels (e.g., GPA, CTC)
        },
      },
      y: {
        ticks: {
          color: "#FFFFFF", // Color for x-axis labels (e.g., GPA, CTC)
        },
      },
    },
    responsive: true,
    plugins: {
      legend: {
        position: "bottom",
        labels: {
          color: "#FFFFFF",
        },
      },
    },
  };

  return (
    <div>
      <h3 className="mb-3" style={{ textAlign: "center" }}>
        Comparison of BTech vs BS Students
      </h3>
      <Bar data={data} options={options} />
    </div>
  );
};

export default BarChart;
