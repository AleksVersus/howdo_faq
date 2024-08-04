// import clsx from 'clsx';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import AvsMainPage from '@site/src/components/AvsMainPage';
import styles from './index.module.css';

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={"Главная"}
      description="Онлайн-справочник по самым часто задаваемым вопросам по QSP | Online guide to the most frequently asked questions about QSP">
      <main className={styles.page}>
        <AvsMainPage />
      </main>
    </Layout>
  );
}
