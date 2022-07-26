/* contact form style */


function contactform() {
    let form_field1 = document.getElementById('id_name');
    let form_field2 = document.getElementById('id_email');
    let form_field3 = document.getElementById('id_message');
  
    if (form_field1 !== null) {
        form_field1.placeholder = 'Your Name', form_field1.className += ' text-dark shadow-none';
        
        form_field1.style.width = '100%';
        form_field1.style.height = '50px';
      };
   

    if (form_field2 !== null) {
        form_field2.placeholder = 'Your Email Address', form_field2.className += ' text-dark shadow-none';
        
        form_field2.style.width = '100%';
        form_field2.style.height = '50px';
      }

      if (form_field3 !== null) {
        form_field3.placeholder = 'How Can We Help?', form_field3.className += ' text-dark shadow-none';
        form_field3.style.width = '100%';
        form_field3.style.height = '199px';
      }
  }
  contactform();