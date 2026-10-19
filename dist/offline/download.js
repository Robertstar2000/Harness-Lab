(() => {
 const button=document.getElementById('download-standalone');
 const status=document.getElementById('standalone-status');
 if(!button)return;
 button.addEventListener('click',async()=>{
  button.disabled=true;status.textContent='Preparing the complete HTML download…';
  try {
   const response=await fetch('offline/manifest.json');if(!response.ok)throw Error('manifest');
   const manifest=await response.json();const parts=[];
   for(let i=0;i<manifest.parts.length;i++){
    const spec=manifest.parts[i];const r=await fetch(spec.url);if(!r.ok)throw Error('part');
    const bytes=await r.arrayBuffer();if(bytes.byteLength!==spec.size)throw Error('size');parts.push(bytes);
    status.textContent='Preparing HTML download: '+Math.round((i+1)/manifest.parts.length*100)+'%';
   }
   const blob=new Blob(parts,{type:'text/html;charset=utf-8'});
   if(blob.size!==manifest.bytes)throw Error('size');
   const digest=await crypto.subtle.digest('SHA-256',await blob.arrayBuffer());
   const hash=Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');
   if(hash!==manifest.sha256)throw Error('integrity');
   const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=manifest.filename;a.click();
   setTimeout(()=>URL.revokeObjectURL(url),60000);
   status.textContent='Downloaded. Open the HTML file in your browser to use the lab and its embedded downloads offline.';
  } catch(error) {status.textContent='The download could not finish. Please try again.';}
  finally {button.disabled=false;}
 });
})();
