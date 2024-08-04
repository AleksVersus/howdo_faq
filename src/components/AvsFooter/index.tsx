import easylib from '@site/src/components/AvsMainPage/css/easylib.module.css';

export default function AvsFooter(): JSX.Element {
    return (
        <aside className={easylib.easyLibPage}>
            <div className={easylib.eBlock}>
            <div className={easylib.avsPageStamp}>
                <p className={easylib.emptyP}>Aleks Versus'HowDo-F.A.Q'2019-${new Date().getFullYear()}. Built with Docusaurus.<br/></p>
                <p className={easylib.emptyP}>Aleks Versus'Game Adventure Making'Really Unimaginable Stories'2019-${new Date().getFullYear()}</p>
            </div></div>
        </aside>
    );
  }