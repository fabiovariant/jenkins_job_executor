export default {
  items: [
    {
      title: true,
      name: 'Ações',
      class: '',
      wrapper: {
        element: '',
        attributes: {}
      }
    },
    {
      name: 'Home',
      url: '/',
      icon: 'icon-home'
    },
    {
      name: 'Relatórios',
      url: '/reports',
      icon: 'icon-doc',
      children: [
        {
          name: 'Executar',
          url: '/reports/new'
        },
        {
          name: 'Histórico',
          url: '/reports/history'
        }
      ]
    },
    {
      name: 'Usuários',
      url: '/user',
      icon: 'icon-user',
      children: [
        {
          name: 'Novo',
          url: '/user/new'
        },
        {
          name: 'Buscar',
          url: '/user/list'
        }
      ]
    },
    {
      name: 'Configuração',
      url: '/user',
      icon: 'icon-settings',
      children: [
        {
          name: 'Jobs',
          url: '/user/new'
        },
        {
          name: 'Usuários',
          url: '/user/list'
        }
      ]
    }
  ]
}
