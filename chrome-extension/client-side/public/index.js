

const displayEvents = () => {
    fetch('http://127.0.0.1:5000/events')
        .then(response => response.json())
        .then(events => {
          console.log(events)
          //events
          const eventhtml = events.map(event2Html).join('\n');
          document.querySelector('#event-cards').innerHTML = eventhtml;
          //fundraiser
          const fundhtml = events.map(fundraiser2Html).join('\n');
          document.querySelector('#fundraiser-cards').innerHTML = fundhtml;
          //campaign
          const camphtml = events.map(camp2Html).join('\n');
          document.querySelector('#campaign-cards').innerHTML = camphtml;
          //all
          document.querySelector('#all-cards').innerHTML = eventhtml + fundhtml + camphtml;
          // keywords
          const listitems = events.map(getkeyword).join('\n');
          document.querySelector('.tags').innerHTML = listitems;
        })
  };

  const getkeyword = event_card =>{
      word = event_card.keyword
      return `<li>${word}</li>`
  }
  
  const event2Html = event_card =>{
    if(event_card.category !== 'event'){
      return ""
    }

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
  

  const fundraiser2Html = event_card =>{
    if(event_card.category !== 'fundraiser'){
      return ""
    }

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

  const camp2Html = event_card =>{
    if(event_card.category !== 'campaign'){
      return ""
    }

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


