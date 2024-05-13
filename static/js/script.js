
// // Example POST method implementation:
// async function postData(url = "", data = {}) {
//     // Default options are marked with *
//     const response = await fetch(url, {
//       method: "POST", // *GET, POST, PUT, DELETE, etc.
//       headers: {
//         "Content-Type": "application/json",
//         // 'Content-Type': 'application/x-www-form-urlencoded',
//        },
//         body: JSON.stringify(data), // body data type must match "Content-Type" header
//     });
//     return response.json(); // parses JSON response into native JavaScript objects
//   }


// document.getElementById('sendbtn').addEventListener('click', function() {
//   questioninput= document.getElementById('questioninput').value;
//   document.getElementById('questioninput').value="";
//   document.querySelector(".right2").style.display = "block"
//   document.querySelector(".right1").style.display = "none"
//   var data = { "question": questioninput };

//   fetch('/api', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify(data)
//   })
//   .then(response => response.json())
//   .then(data => {
//     var result = document.getElementById('solution');
//     result.innerHTML = 'Answer: ' + data.answer;
//   })
//   .catch(error => {
//     console.error('Error:', error);
//   });
// });


sendbtn.addEventListener("click", async ()=>{

    questioninput= document.getElementById('questioninput').value; 
    document.getElementById('questioninput').value="";
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"

    question1.innerHTML = questioninput;
    question2.innerHTML = questioninput;

    // answer displaying  

    const response = await fetch('/generate_response', {
      method: 'POST',
      body: new URLSearchParams({ questioninput }),
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
      }
  });


  const responseData = await response.text();
  // responseDiv.innerHTML = `<p>${responseData}</p>`;
  
   solution.innerHTML = result.responseData
}
 
)