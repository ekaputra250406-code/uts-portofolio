document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Scroll Indicator
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = Math.round((scrollTop / docHeight) * 100);
        const formattedPercent = scrollPercent < 10 ? '0' + scrollPercent : scrollPercent;
        const scrollEl = document.getElementById('scroll-percentage');
        if (scrollEl) scrollEl.innerText = formattedPercent + '%';
    });

    // 2. Typing Cursor (About Section)
    const textToType = "Membangun Solusi Digital.";
    const typingElement = document.getElementById("typing-text");
    let i = 0;
    
    function typeWriter() {
        if (i < textToType.length && typingElement) {
            typingElement.innerHTML += textToType.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    }
    setTimeout(typeWriter, 1000);

    // 3. Custom Cursor (Logika Utama)
    const cursor = document.getElementById('custom-cursor');
    
    if (cursor) {
        // Munculkan kursor saat mouse pertama kali bergerak
        document.addEventListener('mousemove', (e) => {
            cursor.style.display = 'block'; // Tampilkan kursor
            cursor.style.left = e.clientX + 'px'; // Posisi X
            cursor.style.top = e.clientY + 'px';  // Posisi Y
        });

        // Efek saat kursor diarahkan ke elemen interaktif
        const hoverTargets = document.querySelectorAll('a, button, summary, .hover-target');
        
        hoverTargets.forEach(target => {
            target.addEventListener('mouseenter', () => {
                cursor.classList.add('cursor-hover');
            });
            target.addEventListener('mouseleave', () => {
                cursor.classList.remove('cursor-hover');
            });
        });
    } else {
        console.error("Elemen kursor tidak ditemukan!");
    }
});