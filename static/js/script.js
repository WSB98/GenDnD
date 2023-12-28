async function requestImage() {
  function getSelectedOptionText() {
    // Find the checked radio input in the document
    let selectedRadio = document.querySelector('input[name="radio-option"]:checked');
    // If a radio input is selected, find the parent label and return its text content
    if (selectedRadio) {
      let parentLabel = selectedRadio.closest('label');
      if (parentLabel) {
        // The firstChild.nodeValue will give us the text node which is the label content
        return parentLabel.firstChild.nodeValue.trim();
      }
    }
    // Return null if no radio input is selected or if the structure is not as expected
    return null;
  }


  var selectedText = await getSelectedOptionText();
  const textInput = document.getElementById('textInput').value;

  if(textInput.trim() === '') {
    // do nothing
  }
  else {
    document.getElementById('requestImage').disabled = 'true';

    document.getElementById('characterInfo').innerHTML = '<div id="loader" class="loaderAnimation"><svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path id="svgPath" d="M304 48a48 48 0 1 0 -96 0 48 48 0 1 0 96 0zm0 416a48 48 0 1 0 -96 0 48 48 0 1 0 96 0zM48 304a48 48 0 1 0 0-96 48 48 0 1 0 0 96zm464-48a48 48 0 1 0 -96 0 48 48 0 1 0 96 0zM142.9 437A48 48 0 1 0 75 369.1 48 48 0 1 0 142.9 437zm0-294.2A48 48 0 1 0 75 75a48 48 0 1 0 67.9 67.9zM369.1 437A48 48 0 1 0 437 369.1 48 48 0 1 0 369.1 437z"/></svg></div>'

    await fetch('/api/get_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: textInput, type: selectedText}),
    })
      .then((response) => response.json())
      .then(async (data) => {
        document.getElementById('characterInfo').innerHTML = await `<img id="promptImage" alt="Character Token"/>
      <div>
        <h2>Stat Block</h2>
        <p id="statBlock"></p>

        <h2>Backstory</h2>
        <p id="backstory"></p>
      </div>`;
        const link = data.image
        var statblock = data.statblock
        statblock = statblock.replace(/^(Assistant:.*$\n\n)/gm,"") // remove Assistant
        statblock = statblock.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>") //makes text bold
        statblock = statblock.replace(/(?:\r\n|\r|\n)/g, '<br>') //replaces all new lines 
        statblock = statblock.replace(/\*\s/g, '• '); 
        statblock = statblock.replace(/```(.+?)```/g, "<pre><code>$1</code></pre>") //repalces backticks to be pre/code
        //statblock = statblock.split('\n').map(line => `<li>${line}</li>`).join('\n'); //adds bullet points to every line

        var backstory = data.backstory
        backstory = backstory.replace(/^(Assistant:.*$\n\n)/gm,"") // remove Assistant
        backstory = backstory.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>") //makes text bold
        backstory = backstory.replace(/(?:\r\n|\r|\n)/g, '<br>') //replaces all new lines
        backstory = backstory.replace(/\*\s/g, '• '); 
        backstory = backstory.replace(/```(.+?)```/g, "<pre><code>$1</code></pre>") //repalces backticks to be pre/code
        
        //backstory = backstory.split('\n').map(line => `<li>${line}</li>`).join('\n'); //adds bullet points to every line

        const promptImage = document.getElementById('promptImage');
        promptImage.src = link;
        const statblockText = document.getElementById('statBlock');
        statblockText.innerHTML = statblock;
        const backstoryText = document.getElementById('backstory');
        backstoryText.innerHTML = backstory;

        // reformat depending on type of img
        switch(selectedText.toLowerCase()) {
          case 'area':
              promptImage.style.width = '448px';
              promptImage.style.height = '256px';
              promptImage.style.borderRadius = '12px';
            break;
          default:
            promptImage.style.width = '250px';
            promptImage.style.height = '250px';
            promptImage.style.borderRadius = '300px';
        }
        document.getElementById('requestImage').disabled = false;

      });
  }
}

document.getElementById('requestImage').addEventListener('click', requestImage);

function showTooltip(message) {
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = message;
  setTimeout(function () {
    tooltip.style.visibility = "hidden";
  }, 1000);
}


// copy button
var copyButton = document.getElementById("copy_character");
copyButton.addEventListener('click', function() {
  const statBlockText = document.getElementById('statBlock').innerText;
  const backstoryText = document.getElementById('backstory').innerText;
  const combinedText = `**Stat Block:**\n${statBlockText}\n\n**Backstory:**\n${backstoryText}`;

  navigator.clipboard.writeText(combinedText).then(function() {
    console.log('Copying to clipboard was successful!');
    document.getElementById('myTooltip').innerText = 'Copied!🥳🎉';
    setTimeout(() => {
      document.getElementById('myTooltip').innerText = 'Copy';
    },1500)
  }, function(err) {
    console.error('Could not copy text to clipboard: ', err);
  });
});
