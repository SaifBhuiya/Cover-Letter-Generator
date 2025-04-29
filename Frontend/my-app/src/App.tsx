import React from 'react';
import './App.css';
import { useState } from 'react';


function App() {

    const [descInput, setDescInput] = useState<string>('');
    const [resumeInput, setResumeInput] = useState<string>('');
    const [template1, setTemplate1] = useState<string>('');
    const [template2, setTemplate2] = useState<string>('');
    const [templateVisible, setTemplateVisible] = useState<boolean>(false)
    const [istempChosen, setIsTempChosen] = useState<boolean>(false)
    const [tempChosenData, setTempChosenData] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false)


    const handleSubmit = () => {
        setIsLoading(true)
        fetch('http://127.0.0.1:8000/send_text', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                job_desc: descInput,
                resume: resumeInput
            })
        })
            .then(response => response.json())
            .then(data => {
                setTemplate1(data.cover_letter_1)
                setTemplate2(data.cover_letter_2)
                setTemplateVisible(true)
                setIsTempChosen(false)
            })
            .catch(error => console.error('Error:', error))
            .finally(() => setIsLoading(false));
    };


    function generate_CL() {
        if (descInput !== '' && resumeInput !== '') {
            handleSubmit()
        }
        else {
            alert("Please fill up both fields")
        }

    }
    function clear_Input() {
        setDescInput("")
        setResumeInput("")
    }

    function selected_Template(template: string) {
        setIsTempChosen(true)
        setTemplateVisible(false)
        setTempChosenData(template)
    }

    return (
        <div className="App">
            <header>
                Cover Letter Generator
            </header>
            <section id="input_section">

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

            {(templateVisible || istempChosen) && (<hr></hr>)}

            {
                templateVisible && (
                   
                    <section id="template_section">
                       
                        <div className="template">

                            <label>Template 1</label>
                            <textarea className="template_display" value={template1} placeholder="Template 1" disabled></textarea>

                            <button onClick={() => selected_Template(template1)}>
                                Select Option 1
                            </button>

                        </div>

                        <div className="template">

                            <label>Template 2</label>
                            <textarea className="template_display" value={template2} placeholder="Template 2" disabled></textarea>

                            <button onClick={() => selected_Template(template2)}>
                                Select Option 2
                            </button>

                        </div>
                    </section>
                )
            }
            {
                istempChosen && (
                    <section id="final_Cover_Letter">
                      
                        <div className="template">

                            <label>Selected Cover Letter Template</label>
                            <textarea id="final_CL" className="template_display" value={tempChosenData} placeholder="Selected Template" onChange={(e) => setTempChosenData(e.target.value)} ></textarea>
                        </div>
                        <div id="action_buttons">
                            <button onClick={() => setIsTempChosen(false)}>
                                Delete
                            </button>
                        </div>


                    </section>)
            }

            {isLoading && <div className="spinner"></div>}

       




        </div>
    );
}

export default App;
