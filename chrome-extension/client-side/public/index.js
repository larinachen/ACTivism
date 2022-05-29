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
    if(event_card.category === 'event'){
        first_section = `<span>🏙️${event_card.location}</span>`
    }else{
        first_section = `<span>🔗<a href="${event_card.link}" target="_blank">Link</a></span>`
    }

    return `
    <div class="card">
      <div class="main">
        <b>${event_card.title}</b>
        <p>${event_card.description} ... <a href="${event_card.link}" target="_blank">more</a></p> 
        
        <div class="bottombar">
          ${first_section}
          <span>🧑‍🦰${event_card.organizer}</span>
          <span>📅${event_card.time}</span>
        </div>
      </div>
      <img src="${event_card.img_url}">
    </div>

    `;
  }
  
  displayEvents();