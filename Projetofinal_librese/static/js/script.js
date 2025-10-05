document.addEventListener('DOMContentLoaded', () => {
    // Referências aos elementos
    const toggleButton = document.getElementById('theme-toggle-btn');
    const body = document.body;
    const appLogo = document.getElementById('app-logo');

    // Função para aplicar o tema e atualizar o botão
    function applyTheme(theme) {
        if (theme === 'dark') {
            body.classList.add('dark-theme');
            toggleButton.textContent = '☀︎'; // Texto no modo Escuro
            appLogo.src = '/static/images/logo_escuro.png';
            localStorage.setItem('theme', 'dark');
        } else {
            body.classList.remove('dark-theme');
            toggleButton.textContent = '☾'; // Texto no modo Claro
            appLogo.src = '/static/images/logo_claro.png';
            localStorage.setItem('theme', 'light');
        }
    }

    // 1. Lógica ao Clicar no Botão
    toggleButton.addEventListener('click', () => {
        // Verifica se o modo atual é Escuro
        const isDark = body.classList.contains('dark-theme');
        
        // Aplica o tema oposto
        if (isDark) {
            applyTheme('light');
        } else {
            applyTheme('dark');
        }
    });

    // 2. Lógica ao Carregar a Página (Para manter a preferência do usuário)
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme) {
        // Se a preferência foi salva, aplica
        applyTheme(savedTheme);
    } else if (prefersDark) {
        // Se o navegador prefere Escuro e não há preferência salva, aplica Escuro
        applyTheme('dark');
    } else {
        // Padrão: Claro
        applyTheme('light');
    }
});
