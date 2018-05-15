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
      icon: 'icon-doc'
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
          name: 'buscar',
          url: '/user/list'
        }
      ]
    }
  ]
}
