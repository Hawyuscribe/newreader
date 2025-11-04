(function() {
    function createNav(fieldsets) {
        const nav = document.createElement('nav');
        nav.className = 'high-yield-editor-nav';

        const heading = document.createElement('h3');
        heading.textContent = 'Document Outline';
        nav.appendChild(heading);

        const list = document.createElement('ul');
        nav.appendChild(list);

        const buttons = [];

        fieldsets.forEach((fieldset, index) => {
            const legend = fieldset.querySelector('legend');
            const title = legend ? legend.textContent.trim() : `Section ${index + 1}`;
            fieldset.setAttribute('data-hy-label', title);

            const li = document.createElement('li');
            const button = document.createElement('button');
            button.type = 'button';
            button.textContent = title;
            button.addEventListener('click', () => {
                fieldset.scrollIntoView({ behavior: 'smooth', block: 'start' });
                setActive(buttons, button);
            });
            li.appendChild(button);
            list.appendChild(li);
            buttons.push(button);
        });

        const actions = document.createElement('div');
        actions.className = 'high-yield-editor-actions';

        const expand = document.createElement('button');
        expand.type = 'button';
        expand.textContent = 'Expand all';
        expand.addEventListener('click', () => {
            fieldsets.forEach((fieldset) => fieldset.classList.remove('collapsed'));
        });

        const collapse = document.createElement('button');
        collapse.type = 'button';
        collapse.textContent = 'Collapse all';
        collapse.addEventListener('click', () => {
            fieldsets.forEach((fieldset) => fieldset.classList.add('collapsed'));
        });

        actions.appendChild(expand);
        actions.appendChild(collapse);
        nav.appendChild(actions);

        setupScrollSpy(fieldsets, buttons);

        return nav;
    }

    function setupScrollSpy(fieldsets, buttons) {
        if (!('IntersectionObserver' in window)) {
            return;
        }

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        const label = entry.target.getAttribute('data-hy-label');
                        const button = buttons.find((btn) => btn.textContent === label);
                        if (button) {
                            setActive(buttons, button);
                        }
                    }
                });
            },
            {
                rootMargin: '-140px 0px -60%',
                threshold: 0,
            }
        );

        fieldsets.forEach((fieldset) => observer.observe(fieldset));
    }

    function setActive(buttons, active) {
        buttons.forEach((btn) => btn.classList.toggle('active', btn === active));
    }

    function createFloatingToolbar(form) {
        const toolbar = document.createElement('div');
        toolbar.className = 'high-yield-floating-toolbar';

        const focusButton = document.createElement('button');
        focusButton.type = 'button';
        focusButton.textContent = 'Toggle focus';
        focusButton.addEventListener('click', () => {
            document.body.classList.toggle('high-yield-focus-mode');
        });

        const topButton = document.createElement('button');
        topButton.type = 'button';
        topButton.textContent = 'Back to top';
        topButton.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        toolbar.appendChild(focusButton);
        toolbar.appendChild(topButton);
        form.parentElement.appendChild(toolbar);
    }

    function enhanceForm() {
        const contentMain = document.getElementById('content-main');
        if (!contentMain) {
            return;
        }

        const form = contentMain.querySelector('form');
        if (!form) {
            return;
        }

        const fieldsets = Array.from(form.querySelectorAll('fieldset.high-yield-section'));
        if (!fieldsets.length) {
            return;
        }

        document.body.classList.add('high-yield-admin-active');

        const wrapper = document.createElement('div');
        wrapper.className = 'high-yield-editor-form';
        contentMain.insertBefore(wrapper, form);
        wrapper.appendChild(form);

        const nav = createNav(fieldsets);
        contentMain.insertBefore(nav, wrapper);

        createFloatingToolbar(wrapper);

        // Expand collapsed fieldsets by default for a more document-like feel
        fieldsets.forEach((fieldset) => fieldset.classList.remove('collapsed'));
    }

    document.addEventListener('DOMContentLoaded', enhanceForm);
})();
