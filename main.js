// ===== ANKIT JINKWAN PORTFOLIO - MAIN JS =====

document.addEventListener('DOMContentLoaded', () => {
    initParticles();
    initTypedEffect();
    initHeader();
    initMobileMenu();
    initBackToTop();
    initSkillAnimations();
    initProjectFilter();
    initProjectModal();
    initContactForm();
    initScrollAnimations();
});

// ===== PARTICLES =====
function initParticles() {
    const container = document.getElementById('particles');
    if (!container) return;
    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        particle.style.cssText = `
            left: ${Math.random() * 100}%;
            width: ${Math.random() * 4 + 2}px;
            height: ${Math.random() * 4 + 2}px;
            animation-duration: ${Math.random() * 15 + 10}s;
            animation-delay: ${Math.random() * 10}s;
            opacity: ${Math.random() * 0.5 + 0.1};
        `;
        container.appendChild(particle);
    }
}

// ===== TYPED EFFECT =====
function initTypedEffect() {
    const el = document.getElementById('typedText');
    if (!el) return;
    const phrases = ['Full Stack Developer', 'React Developer', 'Node.js Engineer', 'UI/UX Enthusiast', 'Problem Solver'];
    let phraseIndex = 0, charIndex = 0, isDeleting = false;

    function type() {
        const current = phrases[phraseIndex];
        el.textContent = isDeleting
            ? current.substring(0, charIndex--)
            : current.substring(0, charIndex++);

        let delay = isDeleting ? 60 : 110;

        if (!isDeleting && charIndex === current.length + 1) {
            delay = 2000;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            delay = 400;
        }
        setTimeout(type, delay);
    }
    setTimeout(type, 800);
}

// ===== HEADER =====
function initHeader() {
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });

    // Active nav link on scroll
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    window.addEventListener('scroll', () => {
        const scrollPos = window.scrollY + 120;
        sections.forEach(section => {
            if (scrollPos >= section.offsetTop && scrollPos < section.offsetTop + section.offsetHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${section.id}`) link.classList.add('active');
                });
            }
        });
    }, { passive: true });
}

// ===== MOBILE MENU =====
function initMobileMenu() {
    const menuBtn = document.getElementById('menuBtn');
    const navLinks = document.getElementById('navLinks');

    // Create overlay
    const overlay = document.createElement('div');
    overlay.classList.add('nav-overlay');
    document.body.appendChild(overlay);

    function closeMenu() {
        navLinks.classList.remove('active');
        overlay.classList.remove('active');
        menuBtn.innerHTML = '<i class="fas fa-bars"></i>';
        document.body.style.overflow = '';
    }

    menuBtn.addEventListener('click', () => {
        const isOpen = navLinks.classList.contains('active');
        if (isOpen) {
            closeMenu();
        } else {
            navLinks.classList.add('active');
            overlay.classList.add('active');
            menuBtn.innerHTML = '<i class="fas fa-times"></i>';
            document.body.style.overflow = 'hidden';
        }
    });

    overlay.addEventListener('click', closeMenu);
    document.querySelectorAll('.nav-link').forEach(link => link.addEventListener('click', closeMenu));
}

// ===== BACK TO TOP =====
function initBackToTop() {
    const btn = document.getElementById('backToTop');
    window.addEventListener('scroll', () => {
        btn.classList.toggle('active', window.scrollY > 400);
    }, { passive: true });
}

// ===== SKILL BAR ANIMATIONS =====
function initSkillAnimations() {
    const skillItems = document.querySelectorAll('.skill-item');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progress = entry.target.querySelector('.skill-progress');
                const target = entry.target.dataset.skill;
                if (progress && target) {
                    setTimeout(() => {
                        progress.style.width = target + '%';
                    }, 100);
                    observer.unobserve(entry.target);
                }
            }
        });
    }, { threshold: 0.5 });

    skillItems.forEach(item => observer.observe(item));
}

// ===== PROJECT FILTER =====
function initProjectFilter() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.dataset.filter;

            cards.forEach(card => {
                const show = filter === 'all' || card.dataset.category === filter;
                card.style.transition = 'all 0.4s ease';
                if (show) {
                    card.style.display = 'block';
                    setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, 10);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => { card.style.display = 'none'; }, 400);
                }
            });
        });
    });
}

// ===== PROJECT MODAL =====
const projectData = {
    1: { category: 'Web App', title: 'E-Commerce Dashboard', desc: 'A comprehensive dashboard for online retailers featuring real-time analytics, inventory management, order tracking, and customer insights built with React and Node.js.', tags: ['React', 'Node.js', 'MongoDB', 'Express', 'Chart.js'], features: ['Real-time Analytics', 'Inventory Management', 'Order Tracking', 'User Authentication', 'Responsive Design', 'REST API'] },
    2: { category: 'Mobile App', title: 'Health Tracker App', desc: 'A mobile application for tracking daily fitness activities, water intake, calorie counting and health metrics. Features interactive charts and personalized goal setting.', tags: ['React Native', 'Firebase', 'Redux', 'Chart.js'], features: ['Daily Step Counter', 'Water Intake Log', 'Calorie Tracker', 'Progress Charts', 'Push Notifications', 'Offline Support'] },
    3: { category: 'UI/UX', title: 'UI Design System', desc: 'A complete, scalable design system with reusable components, design tokens, and comprehensive documentation to ensure consistent UI development across projects.', tags: ['Figma', 'Storybook', 'CSS3', 'Design Tokens'], features: ['50+ Components', 'Dark/Light Mode', 'Accessibility Ready', 'Storybook Docs', 'Design Tokens', 'Figma Library'] },
    4: { category: 'Web App', title: 'Task Management', desc: 'A collaborative project management tool with Kanban boards, drag-and-drop tasks, team assignments, time tracking and deadline management.', tags: ['Vue.js', 'Express', 'PostgreSQL', 'Socket.io'], features: ['Kanban Boards', 'Drag & Drop', 'Team Collaboration', 'Time Tracking', 'Real-time Updates', 'Email Notifications'] },
    5: { category: 'Mobile App', title: 'Social Media App', desc: 'A social networking platform designed for professionals in creative industries. Features real-time messaging, portfolio sharing and networking tools.', tags: ['Flutter', 'Firebase', 'Dart', 'Cloud Firestore'], features: ['Real-time Chat', 'Portfolio Showcase', 'Follow System', 'Stories Feature', 'Push Notifications', 'Media Upload'] },
    6: { category: 'UI/UX', title: 'Portfolio Redesign', desc: 'A complete visual redesign of a professional photographer portfolio website featuring interactive galleries, smooth GSAP animations and a modern minimalist aesthetic.', tags: ['UI/UX', 'GSAP', 'CSS3', 'JavaScript'], features: ['Smooth Animations', 'Interactive Gallery', 'Lightbox Effect', 'Contact Form', 'SEO Optimized', 'Performance Tuned'] }
};

function initProjectModal() {
    const modal = document.getElementById('projectModal');
    const modalClose = document.getElementById('modalClose');

    document.querySelectorAll('.view-project').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const id = btn.dataset.id;
            const data = projectData[id];
            if (!data) return;

            document.getElementById('modalCategory').textContent = data.category;
            document.getElementById('modalTitle').textContent = data.title;
            document.getElementById('modalDesc').textContent = data.desc;
            document.getElementById('modalImg').src = btn.closest('.project-card').querySelector('img').src;
            document.getElementById('modalImg').alt = data.title;

            const tagsEl = document.getElementById('modalTags');
            tagsEl.innerHTML = data.tags.map(t => `<span class="project-tag">${t}</span>`).join('');

            const featuresEl = document.getElementById('modalFeatures');
            featuresEl.innerHTML = `<h4>Key Features</h4><ul>${data.features.map(f => `<li>${f}</li>`).join('')}</ul>`;

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    modalClose.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });
}

// ===== CONTACT FORM =====
function initContactForm() {
    const form = document.getElementById('contactForm');
    if (!form) return;

    const fields = {
        name: { el: document.getElementById('contactName'), error: document.getElementById('nameError'), validate: v => v.trim().length >= 2 ? '' : 'Name must be at least 2 characters.' },
        email: { el: document.getElementById('contactEmail'), error: document.getElementById('emailError'), validate: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : 'Please enter a valid email.' },
        message: { el: document.getElementById('contactMessage'), error: document.getElementById('messageError'), validate: v => v.trim().length >= 10 ? '' : 'Message must be at least 10 characters.' }
    };

    // Live validation
    Object.values(fields).forEach(({ el, error, validate }) => {
        el.addEventListener('input', () => {
            const msg = validate(el.value);
            error.textContent = msg;
            el.classList.toggle('error', !!msg);
        });
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Validate all fields
        let hasError = false;
        Object.values(fields).forEach(({ el, error, validate }) => {
            const msg = validate(el.value);
            error.textContent = msg;
            el.classList.toggle('error', !!msg);
            if (msg) hasError = true;
        });
        if (hasError) return;

        const submitBtn = document.getElementById('submitBtn');
        const btnText = document.getElementById('btnText');
        const btnLoading = document.getElementById('btnLoading');
        const formStatus = document.getElementById('formStatus');

        // Show loading state
        btnText.style.display = 'none';
        btnLoading.style.display = 'inline-flex';
        submitBtn.disabled = true;
        formStatus.className = 'form-status';
        formStatus.style.display = 'none';

        const payload = {
            name: fields.name.el.value.trim(),
            email: fields.email.el.value.trim(),
            subject: document.getElementById('contactSubject').value.trim() || 'Portfolio Contact',
            message: fields.message.el.value.trim()
        };

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const result = await response.json();

            if (response.ok && result.success) {
                formStatus.textContent = '✅ Message sent! I\'ll get back to you within 24 hours.';
                formStatus.className = 'form-status success';
                form.reset();
                showToast('Message sent successfully!', 'success');
            } else {
                throw new Error(result.message || 'Something went wrong.');
            }
        } catch (err) {
            formStatus.textContent = `❌ ${err.message}. Please try emailing me directly at ankitjhinkwan9@gmail.com`;
            formStatus.className = 'form-status error-msg';
            showToast('Failed to send message.', 'error');
        } finally {
            btnText.style.display = 'inline-flex';
            btnLoading.style.display = 'none';
            submitBtn.disabled = false;
        }
    });
}

// ===== TOAST =====
function showToast(message, type = 'success') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3100);
}

// ===== SCROLL ANIMATIONS =====
function initScrollAnimations() {
    const animateEls = document.querySelectorAll('.project-card, .tech-icon, .info-item, .about-content, .contact-form');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    // Add initial state
    const style = document.createElement('style');
    style.textContent = `
        .project-card, .tech-icon, .info-item, .about-content, .contact-form {
            opacity: 0;
            transform: translateY(25px);
        }
        @keyframes fadeInUp {
            to { opacity: 1; transform: translateY(0); }
        }
    `;
    document.head.appendChild(style);

    animateEls.forEach((el, i) => {
        el.style.animationDelay = `${(i % 3) * 0.1}s`;
        observer.observe(el);
    });
}