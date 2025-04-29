import { useEffect, useState } from "react";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  TextField,
} from "@mui/material";
import api from "./hooks/use-api";

function App() {
  const [error, setError] = useState("");
  const [hypothese, setHypothese] = useState("");
  const [tableaux, setTableaux] = useState<number[][]>([[]]);
  const [variables, setVariables] = useState<string[]>([]);

  const getTable = async () => {
    try {
      const response = await api.post("/", {
        hypothese: hypothese,
      });
      if (response.data.error) {
        setError(response.data.error);
      } else {
        setVariables(response.data.variables);
        setTableaux(response.data.tableaux);
        setError(""); // Clear any previous errors
      }
    } catch (error) {
      // setError(`Erreur lors de l'enregistrement de l'audio: ${error.response ? error.response.data.error : error.message}`);
    }
  };

  useEffect(() => {
    getTable();
  }, [hypothese]);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 3,
      }}
    >
      <TextField
        value={hypothese}
        onChange={(e) => setHypothese(e.target.value)}
        label="Entrer l'hypothese"
        fullWidth
      />
      <TableContainer component={Paper} style={{ width: "98%" }}>
        <Table>
          <TableHead>
            <TableRow className="hover:bg-slate-200">
              {variables.map((vars, index) => (
                <TableCell key={index}>{vars}</TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {tableaux.map((row, index) => (
              <TableRow key={index} className="hover:bg-slate-200">
                {row.map((col, index) => (
                  <TableCell key={index}>{col}</TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default App;
