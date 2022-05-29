const displayEvents = () => {
    fetch('http://127.0.0.1:5000/events')
        .then(response => response.json())
        .then(events => {
          console.log(events)
          const html = events.map(event2Html).join('\n');
          document.querySelector('#cards').innerHTML = html;
        })
  };
  
  const event2Html = event_card =>{
    return `
    <div class="card">
        <p>${event_card.title}</p>
    </div>
    `;
  }
  
  displayEvents();