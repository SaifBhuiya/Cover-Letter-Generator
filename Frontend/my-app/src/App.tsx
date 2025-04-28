import React from 'react';
import './App.css';
import { useState } from 'react';


function App() {

    const [descInput, setDescInput] = useState<string>('');
    const [resumeInput, setResumeInput] = useState<string>('');

   
    const handleSubmit = () => {
        fetch('http://127.0.0.1:8000/send_text', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                job_desc: descInput,
                resume: resumeInput 
            })
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
    };


    function generate_CL() {
        if (descInput !== '' && resumeInput !== '') {
            handleSubmit()
        }
        else {
            alert("none")
        }
        
    }
    function clear_Input() {
        setDescInput("")
        setResumeInput("")
    }

    return (
        <div className="App">
            <header>
                Cover Letter Generator
            </header>

            <section>
                <label>Job Description</label>
                <textarea id="Job_Desc_Input" value={descInput} placeholder="*paste/type Job Description" onChange={(e) => setDescInput(e.target.value)}></textarea>

                <label>Resume Details</label>
                <textarea id="Resume_Input" value={resumeInput} placeholder="*paste/type Resume Details" onChange={(e) => setResumeInput(e.target.value)}></textarea>
                <div>
                    <button onClick={() => generate_CL()}>
                        Generate Cover Letter
                    </button>
                    <button onClick={() => clear_Input()}>
                        Clear
                    </button>
                </div>

            </section>


        </div>
    );
}

export default App;
