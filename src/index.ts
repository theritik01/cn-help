import express from "express";
import cors from "cors";
import fs from "fs";

(async () => {
  const app = express();

  app.use(express.json());
  app.use(express.urlencoded({ extended: true }));
  app.use(cors());

  app.get("/", (req, res) => {
    res.json({ message: "Hello World" });
  });

  app.get("/help", (req, res) => {
    const data = fs.readFileSync("./files/tcpClient.c", "utf8");
    res.send(data);
  });

  app.listen(3000, () => {
    console.log("Server started on port 3000");
  });
})();
