import clsx from 'clsx';
import Link from '@docusaurus/Link';
import easylib from './css/easylib.module.css';
import adapt from './css/adapt.module.css';

export default function AvsMainPage(): JSX.Element {
    return (
        <div className={easylib.avsPageWrapper}>
        <div className={easylib.easyLibPage}>
            <article className={easylib.eBlock}>
            <h1 className={easylib.avsArticleH1}>Онлайн-справочник по самым часто задаваемым вопросам о QSP от Aleks Versus</h1>
            <div className={clsx(easylib.monokaiCode, adapt.contentsWrapper)}>
                <p className={easylib.avsArticleP}>
                    Добро пожаловать на страничку, посвящённую самым часто задаваемым вопросам по QSP.
                </p>
                <p className={easylib.avsArticleP}>Изначально эта страничка создавалась для <span className={easylib.monokaiString}>Справочника по самым часто задаваемым вопросам из темы "Как сделать?" на форуме  <a href="https://qsp.org/index.php?option=com_agora&Itemid=57" title="перейти на форум" target="_blank" className={adapt.hrefPlain}><span className={easylib.monokaiOperator}>QSP.org</span></a></span>, но в течение некоторого времени приросли ещё два раздела, поэтому теперь страничка посвящена более широкому кругу вопросов.
                </p>
                <p className={easylib.avsArticleP}>Онлайн версия справочника переведена на <a href="https://docusaurus.io" className={clsx(adapt.hrefPlain, easylib.monokaiOperator)}>Docusaurus</a>. Известны некоторые проблемы с корректным отображением кода QSP. По мере возможности я буду эти проблемы устранять.</p>
                <p className={easylib.avsArticleP}>Если вы нашли какую-либо ошибку или неточность, просьба заскринить её вместе с адресом страницы и выслать мне на <span className={easylib.monokaiUnFunc}>aleksversus@mail.ru</span>. Это поможет улучшению и исправлению справочника.</p>
                <p className={easylib.avsArticleP}>Ещё вы можете написать мне в VK, это не возбраняется: <a href="https://vk.com/id40090736" className={adapt.hrefPlain} target="_blank"><span className={easylib.monokaiNumeric}>id40090736</span></a>.</p>
                <p className={easylib.avsArticleP}>Онлайн-версия <span className={easylib.monokaiString}>Справочника по самым часто задаваемым вопросам из темы "Как сделать?" на форуме  <a href="https://qsp.org/index.php?option=com_agora&Itemid=57" title="перейти на форум" target="_blank" className={adapt.hrefPlain}><span className={easylib.monokaiOperator}>QSP.org</span></a></span> по прежнему доступна как отдельный раздел.</p>
                <p className={easylib.avsArticleP}>В настоящее время справочник актуализирован под QSP версии 5.8.0, это новый классический плеер и qSpider. Раздел по Quest Navigator исключён, весь код переписан под 5.8.0, многие примеры окажутся нерабочими для плееров версии 5.7.0. Если вам нужен справочник для 5.7.0, есть <a href="https://aleksversus.github.io/howdo_faq/release/F.A.Q.HowDo for QSP 5.7.0.zip" className={adapt.hrefPlain}><span className={easylib.monokaiOperator}>копия онлайн-версии</span></a>, а так же старые релизы офлайн-версии.</p>
                <p className={adapt.pWarning}>Кнопка "Содержание" пока не работает ни в одном разделе.</p>
                
                <h6 className={easylib.avsArticleH6}><span className={easylib.monokaiFunc}>Справочник по самым часто задаваемым вопросам из темы "Как сделать?":</span></h6>
               
                <ul className={easylib.cmd} >
                    <li className={easylib.cmd_item}>
                        <Link 
                            className={adapt.hrefPlain}
                            to="/docs/howdo/intro">
                            <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Важное предисловие"</span>
                        </Link>
                    </li>
                    <li className={easylib.cmd_item}>
                        <Link 
                            className={adapt.hrefPlain}
                            to="https://dev.qsp.org/ru/docs/language/qsp-keywords/">
                            <span className={easylib.monokaiOperator}>goto</span> <span className={easylib.monokaiString}>"Зарезервированные слова, спецсимволы и системные переменные"</span>
                        </Link>
                    </li>
                    <li className={easylib.cmd_item}>
                        <Link 
                            className={adapt.hrefPlain}
                            to="/docs/howdo/links">
                            <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Источники и дополнительные материалы"</span>
                        </Link>
                    </li>
                </ul>
                <h6 className={easylib.avsArticleH6}><span className={easylib.monokaiFunc}>Дополнительно:</span></h6>
                    <span className={easylib.monokaiComment}>! Тема, посвящённая справочнику, на форуме QSP.org:</span>
                        <ul className={easylib.cmd}>
                            <li className={easylib.cmd_item}>
                                <a href="http://qsp.su/index.php?option=com_agora&task=topic&id=1280&p=1&prc=25&Itemid=57#p28373" className={adapt.hrefPlain} target="_blank"><span className={easylib.monokaiOperator}>goto</span> <span className={easylib.monokaiString}>"qsp.org/F.A.Q.: Часто задаваемые вопросы из темы "Как сделать?""</span></a>
                            </li>
                        </ul>
                    <span className={easylib.monokaiComment}>! Скачать последнюю версию офлайн-справочника вы всегда можете со страницы релизов:</span>
                <ul className={easylib.cmd}>
                    <li>
                        <a href="https://github.com/AleksVersus/howdo_faq/releases" className={adapt.hrefPlain} target="_blank"><span className={easylib.monokaiOperator}>goto</span> <span className={easylib.monokaiString}>"GitHub/HowDo_FAQ/releases"</span></a> (Редакция от 03.11.2021.)
                    </li>
                </ul>
                <h6 className={easylib.avsArticleH6}><span className={easylib.monokaiFunc}>Статьи по QSP:</span></h6>  
                        <ul className={easylib.cmd}>
                            <li className={easylib.cmd_item}>
                                <Link 
                                    className={adapt.hrefPlain}
                                    to="/docs/articles/type_casting">
                                    <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Преобразование типов в QSP"</span>
                                </Link>
                            </li>
                            <li className={easylib.cmd_item}>
                                <Link 
                                    className={adapt.hrefPlain}
                                    to="/docs/articles/arrays_580/">
                                    <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Изменения в работе массивов в плеерах версии 5.8.0"</span>
                                </Link>
                            </li>
                            <li className={easylib.cmd_item}>
                                <Link 
                                    className={adapt.hrefPlain}
                                    to="/docs/news/news_content">
                                    <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Нововведения в QSP"</span>
                                </Link>
                            </li>
                            <li className={easylib.cmd_item}>
                                <Link 
                                    className={adapt.hrefPlain}
                                    to="/docs/articles/qspider_0120/">
                                    <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Сводная статья по qSpider версии 0.12.0"</span>
                                </Link>
                            </li>
                            <li className={easylib.cmd_item}>
                                <Link 
                                    className={adapt.hrefPlain}
                                    to="/docs/articles/config_classic_570">
                                    <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Структура qspgui.cfg классического плеера 5.7.0"</span>
                                </Link>
                            </li>
                            <li className={easylib.cmd_item}>
                                <Link 
                                    className={adapt.hrefPlain}
                                    to="/docs/articles/operators_funcs_args/">
                                    <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Операторы, функции и аргументы в QSP. GOSUB, FUNC, ARGS"</span>
                                </Link>
                            </li>
                        </ul>
                <h6 className={easylib.avsArticleH6}><span className={easylib.monokaiFunc}>Информ-Архив QSP:</span></h6>
                    <span className={easylib.monokaiComment}>! устаревшие статьи, которые пока ещё существуют и на QSP.org,<br/>! но в скором времени могут быть удалены оттуда.</span>
                    <ul className={easylib.cmd}>
                            <li className={easylib.cmd_item}>
                                <Link 
                                    className={adapt.hrefPlain}
                                    to="/docs/informarch/intro">
                                    <span className={easylib.monokaiOperator}>jump</span> <span className={easylib.monokaiString}>"Оглавление"</span>
                                </Link>
                            </li>
                        </ul>
     
                
                <h6 className={easylib.avsArticleH6}><span className={easylib.monokaiFunc}>Мои ресурсы:</span></h6>
                <ul className={easylib.cmd}>
                    <li className={easylib.cmd_item}>
                    <a href="http://aleksversus.narod.ru" className={adapt.hrefPlain} target="_blank" title="Открыть в новой вкладке"><span className={easylib.monokaiOperator}>goto</span> <span className={easylib.monokaiString}>"aleksversus.narod.ru"</span> <span className={easylib.monokaiOperator}>&amp;</span> <span className={easylib.monokaiComment}>! мой сайт</span></a>
                    </li>
                    <li className={easylib.cmd_item}>
                    <a href="https://boosty.to/aleksversus" className={adapt.hrefPlain} target="_blank" title="Открыть в новой вкладке"><span className={easylib.monokaiOperator}>goto</span> <span className={easylib.monokaiString}>"boosty/aleksversus"</span> <span className={easylib.monokaiOperator}>&amp;</span> <span className={easylib.monokaiComment}>! мой блог на BOOSTY</span></a>
                    </li>
                    <li className={easylib.cmd_item}>
                    <a href="https://www.donationalerts.com/r/aleksversus" className={adapt.hrefPlain} target="_blank" title="Открыть в новой вкладке"><span className={easylib.monokaiOperator}>goto</span> <span className={easylib.monokaiString}>"donationalerts/aleksversus"</span> <span className={easylib.monokaiOperator}>&amp;</span> <span className={easylib.monokaiComment}>! если хотите поддержать меня копеечкой</span></a>
                    </li>
                </ul>
            </div>
            </article>
        </div>
    </div>
    );
  }
