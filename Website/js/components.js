document.addEventListener("DOMContentLoaded", function() {
    const components = [
        { id: 'leacli-header', file: '/components/header.html' },
        { id: 'leacli-cta', file: '/components/cta.html' },
        { id: 'leacli-footer', file: '/components/footer.html' },
        { id: 'leacli-modal-menu', file: '/components/modal-menu.html' },
        { id: 'leacli-mobile-menu', file: '/components/mobile-menu.html' },
        { id: 'leacli-modal-form', file: '/components/modal-form.html' }
    ];

    const loadPromises = components.map(comp => {
        const placeholder = document.getElementById(comp.id);
        if (placeholder) {
            return fetch(comp.file)
                .then(response => {
                    if (!response.ok) throw new Error('Network response was not ok');
                    return response.text();
                })
                .then(html => {
                    placeholder.outerHTML = html; // Replace the div with the actual HTML component
                })
                .catch(error => console.error('Error loading component ' + comp.file, error));
        }
        return Promise.resolve();
    });

    // When all components are loaded, UIkit will automatically catch up thanks to MutationObservers
    Promise.all(loadPromises).then(() => {
        // Optional: Trigger custom events if other scripts need to wait for components
        document.dispatchEvent(new Event('componentsLoaded'));
    });
});
