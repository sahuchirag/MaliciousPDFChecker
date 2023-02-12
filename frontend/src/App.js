import React, { useState } from "react";
import axios from "axios";
import "./App.css";

export default function App() {
	const [answer, setAnswer] = useState("");
	const [word, setWord] = useState("");
	const [image, setImage] = useState({ preview: '', data: '' })
	const [image2, setImage2] = useState({ preview: '', data: '' })

	const handleFileChange = (e, num) => {
		if (!num) {
			const img = {
				preview: URL.createObjectURL(e.target.files[0]),
				data: e.target.files[0],
			}
			setImage(img)
		}

		else {
			const img2 = {
				preview: URL.createObjectURL(e.target.files[0]),
				data: e.target.files[0],
			}
			setImage2(img2)
		}
	}

	function handleSubmit(num) {
		if (!num) {
			if (!image.data) {
				alert("Please upload a PDF!");
			}

			else {
				let formData = new FormData();
				formData.append('file', image.data);
				print(formData)
				axios
					.post("http://127.0.0.1:2000", formData)
					.then((res) => {
						setAnswer(res.data);
					})
					.catch((err) => {
						console.log(err.response);
					});
			}
		}
	}

	return (
		<div className="mainContainer">
		<div className="dataContainer">
		<div className="header">
		<span role="img" aria-label="information">
		👋
		</span>{" "}
		Hey there!
		</div>

		<div className="bio">Welcome to Malicious PDF Identifier!</div>

		<div className="bio">
		<form>
		<div className="instruct">Upload a PDF to check below.</div>
		{/* {image.preview && <img src={image.preview} width='100' height='100' />} */}
		<hr></hr>
		<input type='file' name='file' accept=".pdf" onChange={(e) => handleFileChange(e, 0)}></input>
		</form>
		</div>

		<button className="speedButton" onClick={() => handleSubmit(0)}>
		Check PDF.
		</button>
		</div>
		</div>
	);
}

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
