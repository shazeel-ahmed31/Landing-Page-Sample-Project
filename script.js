document.addEventListener('DOMContentLoaded',()=>{
 for(const [formId,statusId,message] of [['contactForm','formStatus','Demo complete. Your message was not sent or stored.'],['newsletterForm','newsletterStatus','Demo complete. No newsletter subscription was created.']]){
  const form=document.getElementById(formId);form.querySelector('button').disabled=false;
  form.addEventListener('submit',event=>{event.preventDefault();for(const field of form.querySelectorAll('[required]'))field.setCustomValidity(field.value.trim()?'':'Enter a value.');if(form.reportValidity())document.getElementById(statusId).textContent=message;});
  form.querySelectorAll('input,textarea').forEach(field=>field.addEventListener('input',()=>field.setCustomValidity('')));
 }
});
