import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

let footer = `<aside class="footerBlock">
<div class="eBlock">
<div class="avsPageStamp">
    <p class="emptyP">Aleks Versus'HowDo-F.A.Q'2019-${new Date().getFullYear()}. Built with Docusaurus.<br/></p>
    <p class="emptyP">Aleks Versus'Game Adventure Making'Really Unimaginable Stories'2019-${new Date().getFullYear()}</p>
</div></div>
</aside>`

const config: Config = {
  title: 'Справочник | F.A.Q.',
  tagline: 'Справочные материалы и статьи по QSP',
  favicon: 'res/favicon.ico',
  // stylesheets: ['@site/src/components/AvsMainPage/css/easylib.module.css'],

  // Set the production url of your site here
  url: 'https://aleksversus.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/howdo_faq/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'https://github.com/AleksVersus', // Usually your GitHub org/user name.
  projectName: 'howdo_faq', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'ru',
    locales: ['ru'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: false,
        theme: {
          customCss: [
            './src/css/custom.css',
            './src/css/footer.css',
            './src/css/qsp-syntax.css'
          ],
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'res/favicon.ico',
    navbar: {
      title: 'Главная',
      // logo: {
      //   alt: 'My Site Logo',
      //   src: 'img/logo.svg',
      // },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'howdoSidebar',
          position: 'left',
          label: 'Как сделать? F.A.Q.',
        },
        {
          type: 'docSidebar',
          sidebarId: 'articlesSidebar',
          position: 'left',
          label: 'Статьи',
        },
        {
          type: 'docSidebar',
          sidebarId: 'informArchSidebar',
          position: 'right',
          label: 'Информ-Архив',
        },
        // {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://aleksversus.github.io/howdo_faq/',
          label: 'GitHub/HowDo_F.A.Q',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        // {
        //   title: 'Docs',
        //   items: [
        //     {
        //       label: 'Tutorial',
        //       to: '/docs/intro',
        //     },
        //   ],
        // },
        // {
        //   title: 'Community',
        //   items: [
        //     {
        //       label: 'Stack Overflow',
        //       href: 'https://stackoverflow.com/questions/tagged/docusaurus',
        //     },
        //     {
        //       label: 'Discord',
        //       href: 'https://discordapp.com/invite/docusaurus',
        //     },
        //     {
        //       label: 'Twitter',
        //       href: 'https://twitter.com/docusaurus',
        //     },
        //   ],
        // },
        // {
        //   title: 'More',
        //   items: [
        //     {
        //       label: 'Blog',
        //       to: '/blog',
        //     },
        //     {
        //       label: 'GitHub',
        //       href: 'https://github.com/facebook/docusaurus',
        //     },
        //   ],
        // },
      ],
      copyright: footer,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
