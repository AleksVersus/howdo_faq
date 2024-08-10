import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/markdown-page',
    component: ComponentCreator('/markdown-page', '3d7'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '99e'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '9e2'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '945'),
            routes: [
              {
                path: '/docs/articles/arrays_580/',
                component: ComponentCreator('/docs/articles/arrays_580/', '228'),
                exact: true,
                sidebar: "articlesSidebar"
              },
              {
                path: '/docs/articles/config_classic_570',
                component: ComponentCreator('/docs/articles/config_classic_570', 'c7e'),
                exact: true,
                sidebar: "articlesSidebar"
              },
              {
                path: '/docs/articles/news_580',
                component: ComponentCreator('/docs/articles/news_580', '485'),
                exact: true,
                sidebar: "articlesSidebar"
              },
              {
                path: '/docs/articles/operators_funcs_args/',
                component: ComponentCreator('/docs/articles/operators_funcs_args/', '261'),
                exact: true,
                sidebar: "articlesSidebar"
              },
              {
                path: '/docs/articles/qspider_0120/',
                component: ComponentCreator('/docs/articles/qspider_0120/', '797'),
                exact: true,
                sidebar: "articlesSidebar"
              },
              {
                path: '/docs/articles/stylization_manifest',
                component: ComponentCreator('/docs/articles/stylization_manifest', '3b4'),
                exact: true,
                sidebar: "articlesSidebar"
              },
              {
                path: '/docs/articles/type_casting',
                component: ComponentCreator('/docs/articles/type_casting', '42e'),
                exact: true,
                sidebar: "articlesSidebar"
              },
              {
                path: '/docs/category/руководство---основы',
                component: ComponentCreator('/docs/category/руководство---основы', '3ee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/category/руководство---остальное',
                component: ComponentCreator('/docs/category/руководство---остальное', 'd05'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/intro',
                component: ComponentCreator('/docs/ds/intro', '1af'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-basics/congratulations',
                component: ComponentCreator('/docs/ds/tutorial-basics/congratulations', 'fe2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-basics/create-a-blog-post',
                component: ComponentCreator('/docs/ds/tutorial-basics/create-a-blog-post', '11d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-basics/create-a-document',
                component: ComponentCreator('/docs/ds/tutorial-basics/create-a-document', '8c6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-basics/create-a-page',
                component: ComponentCreator('/docs/ds/tutorial-basics/create-a-page', 'b30'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-basics/deploy-your-site',
                component: ComponentCreator('/docs/ds/tutorial-basics/deploy-your-site', '67e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-basics/markdown-features',
                component: ComponentCreator('/docs/ds/tutorial-basics/markdown-features', '409'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-extras/code blocks',
                component: ComponentCreator('/docs/ds/tutorial-extras/code blocks', '6ca'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-extras/manage-docs-versions',
                component: ComponentCreator('/docs/ds/tutorial-extras/manage-docs-versions', '568'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ds/tutorial-extras/translate-your-site',
                component: ComponentCreator('/docs/ds/tutorial-extras/translate-your-site', '5ae'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/actions_direct',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/actions_direct', '1ff'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/arrays_comparison',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/arrays_comparison', 'd3e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/check_for_even',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/check_for_even', '4ce'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/choose_random_card',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/choose_random_card', 'dab'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/data_sorting',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/data_sorting', '395'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/decomposing_in_terms',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/decomposing_in_terms', '1f1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/goto_back',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/goto_back', 'f75'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/how_much_variables',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/how_much_variables', '16d'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/html_clear_preformatting',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/html_clear_preformatting', '0a1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/html_with_usehtml',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/html_with_usehtml', 'c4d'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/item_drop_chance',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/item_drop_chance', '0ac'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/make_book',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/make_book', '6ae'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/make_chest',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/make_chest', '5d0'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/make_notes',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/make_notes', 'a77'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/make_percents',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/make_percents', '21c'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/maximal_variable',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/maximal_variable', '55f'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/one_off_location',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/one_off_location', '9d6'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/print_text_top',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/print_text_top', 'de9'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/random_action',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/random_action', '8d6'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/random_goto',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/random_goto', '832'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/random_item',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/random_item', 'e7f'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/replace_text_part',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/replace_text_part', '80e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/simple_fill_array',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/simple_fill_array', 'df6'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/concrete_tasks/text_thinning',
                component: ComponentCreator('/docs/howdo/contents/concrete_tasks/text_thinning', '74d'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/condition/conditional_action',
                component: ComponentCreator('/docs/howdo/contents/condition/conditional_action', 'cc7'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/condition/conditional_message',
                component: ComponentCreator('/docs/howdo/contents/condition/conditional_message', 'b6f'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/condition/conditional_text',
                component: ComponentCreator('/docs/howdo/contents/condition/conditional_text', '442'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/condition/desactivated_action',
                component: ComponentCreator('/docs/howdo/contents/condition/desactivated_action', 'bc8'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/condition/number_as_condition',
                component: ComponentCreator('/docs/howdo/contents/condition/number_as_condition', 'e87'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/condition/simplificate_condition',
                component: ComponentCreator('/docs/howdo/contents/condition/simplificate_condition', '2f8'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/condition/xor',
                component: ComponentCreator('/docs/howdo/contents/condition/xor', 'fbb'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/counter/distributed_cycle',
                component: ComponentCreator('/docs/howdo/contents/counter/distributed_cycle', '78d'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/counter/promise_action',
                component: ComponentCreator('/docs/howdo/contents/counter/promise_action', '7d8'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/counter/promise_goto',
                component: ComponentCreator('/docs/howdo/contents/counter/promise_goto', '215'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/counter/realtime_variable_change',
                component: ComponentCreator('/docs/howdo/contents/counter/realtime_variable_change', '0ae'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/dynamic/cycling_actions_create',
                component: ComponentCreator('/docs/howdo/contents/dynamic/cycling_actions_create', 'f17'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/dynamic/not_work_dynamic',
                component: ComponentCreator('/docs/howdo/contents/dynamic/not_work_dynamic', '286'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/dynamic/random_variable',
                component: ComponentCreator('/docs/howdo/contents/dynamic/random_variable', '942'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/dynamic/why_need_dynamic',
                component: ComponentCreator('/docs/howdo/contents/dynamic/why_need_dynamic', '4a6'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/ascii_graphics',
                component: ComponentCreator('/docs/howdo/contents/extended/ascii_graphics', '14c'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/debugger',
                component: ComponentCreator('/docs/howdo/contents/extended/debugger', '9bd'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/hack_protection',
                component: ComponentCreator('/docs/howdo/contents/extended/hack_protection', 'ac3'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/how_insert_video',
                component: ComponentCreator('/docs/howdo/contents/extended/how_insert_video', '40d'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/how_use_keyboard',
                component: ComponentCreator('/docs/howdo/contents/extended/how_use_keyboard', 'e0e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/letter_by_letter',
                component: ComponentCreator('/docs/howdo/contents/extended/letter_by_letter', '543'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/print_text_bottom_top',
                component: ComponentCreator('/docs/howdo/contents/extended/print_text_bottom_top', 'fd3'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/skip_chapters',
                component: ComponentCreator('/docs/howdo/contents/extended/skip_chapters', '3a0'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/variables_refresh',
                component: ComponentCreator('/docs/howdo/contents/extended/variables_refresh', '7db'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/extended/what_device',
                component: ComponentCreator('/docs/howdo/contents/extended/what_device', '113'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/hyperlink/how_make_hypelinks',
                component: ComponentCreator('/docs/howdo/contents/hyperlink/how_make_hypelinks', '315'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/hyperlink/hyperlinks_color',
                component: ComponentCreator('/docs/howdo/contents/hyperlink/hyperlinks_color', 'a00'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/hyperlink/hyperlinks_complex_code',
                component: ComponentCreator('/docs/howdo/contents/hyperlink/hyperlinks_complex_code', '51a'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/hyperlink/hyperlinks_none_underline',
                component: ComponentCreator('/docs/howdo/contents/hyperlink/hyperlinks_none_underline', '9b3'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/changable_image',
                component: ComponentCreator('/docs/howdo/contents/images/changable_image', 'e21'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/clickable_image',
                component: ComponentCreator('/docs/howdo/contents/images/clickable_image', '82e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/gif_in_game',
                component: ComponentCreator('/docs/howdo/contents/images/gif_in_game', '0d1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/image_in_action',
                component: ComponentCreator('/docs/howdo/contents/images/image_in_action', 'c4f'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/image_in_game',
                component: ComponentCreator('/docs/howdo/contents/images/image_in_game', 'd3f'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/image_to_background',
                component: ComponentCreator('/docs/howdo/contents/images/image_to_background', '391'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/images_in_layers',
                component: ComponentCreator('/docs/howdo/contents/images/images_in_layers', '388'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/images/random_image',
                component: ComponentCreator('/docs/howdo/contents/images/random_image', 'af6'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/input/use_input_string',
                component: ComponentCreator('/docs/howdo/contents/input/use_input_string', '3af'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/input/why_need_input_string',
                component: ComponentCreator('/docs/howdo/contents/input/why_need_input_string', 'ce9'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/actions_highlight',
                component: ComponentCreator('/docs/howdo/contents/interface/actions_highlight', 'd66'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/actions_unselect',
                component: ComponentCreator('/docs/howdo/contents/interface/actions_unselect', '4f8'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/background_color',
                component: ComponentCreator('/docs/howdo/contents/interface/background_color', 'd51'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/beautiful_background',
                component: ComponentCreator('/docs/howdo/contents/interface/beautiful_background', '18b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/fixed_preview_window',
                component: ComponentCreator('/docs/howdo/contents/interface/fixed_preview_window', 'ad7'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/refint',
                component: ComponentCreator('/docs/howdo/contents/interface/refint', '8f8'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/smooth_text_fade_in',
                component: ComponentCreator('/docs/howdo/contents/interface/smooth_text_fade_in', '572'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/text_formatting',
                component: ComponentCreator('/docs/howdo/contents/interface/text_formatting', 'd12'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/user_font',
                component: ComponentCreator('/docs/howdo/contents/interface/user_font', '0d5'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/window_background',
                component: ComponentCreator('/docs/howdo/contents/interface/window_background', '824'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/windows_settings',
                component: ComponentCreator('/docs/howdo/contents/interface/windows_settings', '78b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/interface/windows_sizes',
                component: ComponentCreator('/docs/howdo/contents/interface/windows_sizes', '646'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/add_item',
                component: ComponentCreator('/docs/howdo/contents/items/add_item', '8c4'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/add_item_in_pos',
                component: ComponentCreator('/docs/howdo/contents/items/add_item_in_pos', 'fbe'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/del_all_items',
                component: ComponentCreator('/docs/howdo/contents/items/del_all_items', '7da'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/del_item',
                component: ComponentCreator('/docs/howdo/contents/items/del_item', '5fc'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/images_item',
                component: ComponentCreator('/docs/howdo/contents/items/images_item', 'a29'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/item_without_inventory',
                component: ComponentCreator('/docs/howdo/contents/items/item_without_inventory', 'ca4'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/multi_leveled_backpack',
                component: ComponentCreator('/docs/howdo/contents/items/multi_leveled_backpack', 'abc'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/one_named_items',
                component: ComponentCreator('/docs/howdo/contents/items/one_named_items', 'd8c'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/onobjadd',
                component: ComponentCreator('/docs/howdo/contents/items/onobjadd', '62b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/onobjsel',
                component: ComponentCreator('/docs/howdo/contents/items/onobjsel', '3cf'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/replace_item',
                component: ComponentCreator('/docs/howdo/contents/items/replace_item', 'e75'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/stackable_items',
                component: ComponentCreator('/docs/howdo/contents/items/stackable_items', '48b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/two_lists_of_items',
                component: ComponentCreator('/docs/howdo/contents/items/two_lists_of_items', '93e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/items/unselect',
                component: ComponentCreator('/docs/howdo/contents/items/unselect', 'bc9'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/alignment',
                component: ComponentCreator('/docs/howdo/contents/layout/alignment', 'ee1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/fade_in_fade_out',
                component: ComponentCreator('/docs/howdo/contents/layout/fade_in_fade_out', 'ae1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/image_reflection',
                component: ComponentCreator('/docs/howdo/contents/layout/image_reflection', 'ae8'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/image_size',
                component: ComponentCreator('/docs/howdo/contents/layout/image_size', '030'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/items_table',
                component: ComponentCreator('/docs/howdo/contents/layout/items_table', '67e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/map_area',
                component: ComponentCreator('/docs/howdo/contents/layout/map_area', 'a0b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/text_over_image',
                component: ComponentCreator('/docs/howdo/contents/layout/text_over_image', '5f1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/two_column_text',
                component: ComponentCreator('/docs/howdo/contents/layout/two_column_text', 'c93'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/under_table_artefacts',
                component: ComponentCreator('/docs/howdo/contents/layout/under_table_artefacts', '069'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/layout/windows_border',
                component: ComponentCreator('/docs/howdo/contents/layout/windows_border', '929'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/libs_n_mods/file_is_exist',
                component: ComponentCreator('/docs/howdo/contents/libs_n_mods/file_is_exist', '428'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/libs_n_mods/inclib_openqst',
                component: ComponentCreator('/docs/howdo/contents/libs_n_mods/inclib_openqst', '315'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/libs_n_mods/launcher',
                component: ComponentCreator('/docs/howdo/contents/libs_n_mods/launcher', '1f7'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/libs_n_mods/qproj_file',
                component: ComponentCreator('/docs/howdo/contents/libs_n_mods/qproj_file', '96e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/libs_n_mods/tmp_file',
                component: ComponentCreator('/docs/howdo/contents/libs_n_mods/tmp_file', '73d'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/menu/args_to_menu_item',
                component: ComponentCreator('/docs/howdo/contents/menu/args_to_menu_item', 'bcf'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/menu/context_menu',
                component: ComponentCreator('/docs/howdo/contents/menu/context_menu', 'd1e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/menu/different_menus',
                component: ComponentCreator('/docs/howdo/contents/menu/different_menus', '22b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/menu/image_in_menu',
                component: ComponentCreator('/docs/howdo/contents/menu/image_in_menu', '8a6'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/menu/menu_in_hyperlinks',
                component: ComponentCreator('/docs/howdo/contents/menu/menu_in_hyperlinks', '41b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/menu/menu_of_item',
                component: ComponentCreator('/docs/howdo/contents/menu/menu_of_item', 'ffd'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/menu/menu_separator',
                component: ComponentCreator('/docs/howdo/contents/menu/menu_separator', 'b35'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/msg_input/modal_alert_msg',
                component: ComponentCreator('/docs/howdo/contents/msg_input/modal_alert_msg', '27f'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/msg_input/modal_confirm',
                component: ComponentCreator('/docs/howdo/contents/msg_input/modal_confirm', '0f2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/msg_input/modal_input_variants',
                component: ComponentCreator('/docs/howdo/contents/msg_input/modal_input_variants', '1b2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/msg_input/modal_prompt',
                component: ComponentCreator('/docs/howdo/contents/msg_input/modal_prompt', '08a'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/msg_input/players_input_name',
                component: ComponentCreator('/docs/howdo/contents/msg_input/players_input_name', '9e9'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/attrib_height',
                component: ComponentCreator('/docs/howdo/contents/not_work/attrib_height', '4c7'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/condition',
                component: ComponentCreator('/docs/howdo/contents/not_work/condition', 'bd0'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/end',
                component: ComponentCreator('/docs/howdo/contents/not_work/end', 'c8b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/fractional_numbers',
                component: ComponentCreator('/docs/howdo/contents/not_work/fractional_numbers', '3f0'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/iif',
                component: ComponentCreator('/docs/howdo/contents/not_work/iif', 'cce'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/jump',
                component: ComponentCreator('/docs/howdo/contents/not_work/jump', '6aa'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/manylines_code',
                component: ComponentCreator('/docs/howdo/contents/not_work/manylines_code', '762'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/manylines_condition',
                component: ComponentCreator('/docs/howdo/contents/not_work/manylines_condition', 'd90'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/map_area',
                component: ComponentCreator('/docs/howdo/contents/not_work/map_area', 'c4e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/star_print_line',
                component: ComponentCreator('/docs/howdo/contents/not_work/star_print_line', '00a'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/not_work/tags',
                component: ComponentCreator('/docs/howdo/contents/not_work/tags', '4ef'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/onnewloc/args_translate',
                component: ComponentCreator('/docs/howdo/contents/onnewloc/args_translate', 'fbd'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/onnewloc/back_button',
                component: ComponentCreator('/docs/howdo/contents/onnewloc/back_button', 'fd6'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/onnewloc/system_locations',
                component: ComponentCreator('/docs/howdo/contents/onnewloc/system_locations', '874'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/quest generator/code_folding',
                component: ComponentCreator('/docs/howdo/contents/quest generator/code_folding', 'bf2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/quest generator/keybindings',
                component: ComponentCreator('/docs/howdo/contents/quest generator/keybindings', 'b08'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/restriction/actions_numbers',
                component: ComponentCreator('/docs/howdo/contents/restriction/actions_numbers', 'd80'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/restriction/inclib_numbers',
                component: ComponentCreator('/docs/howdo/contents/restriction/inclib_numbers', '9a4'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/restriction/varnames',
                component: ComponentCreator('/docs/howdo/contents/restriction/varnames', '6f4'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/saves/checkpoints',
                component: ComponentCreator('/docs/howdo/contents/saves/checkpoints', 'efd'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/saves/forbidden_saves',
                component: ComponentCreator('/docs/howdo/contents/saves/forbidden_saves', '34e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/saves/not_load_saves',
                component: ComponentCreator('/docs/howdo/contents/saves/not_load_saves', '2fa'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/saves/two_save_files',
                component: ComponentCreator('/docs/howdo/contents/saves/two_save_files', 'afa'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/sound/break_soundtrack',
                component: ComponentCreator('/docs/howdo/contents/sound/break_soundtrack', 'e5a'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/sound/insert_soundtrack',
                component: ComponentCreator('/docs/howdo/contents/sound/insert_soundtrack', 'ac9'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/sound/loop_soundtrack',
                component: ComponentCreator('/docs/howdo/contents/sound/loop_soundtrack', '41e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/sound/playlists',
                component: ComponentCreator('/docs/howdo/contents/sound/playlists', '532'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/sound/soundtrack_restart',
                component: ComponentCreator('/docs/howdo/contents/sound/soundtrack_restart', '278'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/sound/turn_down',
                component: ComponentCreator('/docs/howdo/contents/sound/turn_down', '9a2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/sound/two_soundtracks',
                component: ComponentCreator('/docs/howdo/contents/sound/two_soundtracks', 'bc4'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_command/clr',
                component: ComponentCreator('/docs/howdo/contents/what_command/clr', '2ec'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_command/curloc',
                component: ComponentCreator('/docs/howdo/contents/what_command/curloc', '17c'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_command/exit_command',
                component: ComponentCreator('/docs/howdo/contents/what_command/exit_command', '171'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_command/print_line_in_stat_window',
                component: ComponentCreator('/docs/howdo/contents/what_command/print_line_in_stat_window', 'bc4'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/dollar_sign',
                component: ComponentCreator('/docs/howdo/contents/what_dif/dollar_sign', '9ff'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/dynamic_dyneval',
                component: ComponentCreator('/docs/howdo/contents/what_dif/dynamic_dyneval', 'c86'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/goto_gosub',
                component: ComponentCreator('/docs/howdo/contents/what_dif/goto_gosub', '7da'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/gt_goto',
                component: ComponentCreator('/docs/howdo/contents/what_dif/gt_goto', 'a3c'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/inclib_openqst/',
                component: ComponentCreator('/docs/howdo/contents/what_dif/inclib_openqst/', '3e3'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/pl_implicit_operator',
                component: ComponentCreator('/docs/howdo/contents/what_dif/pl_implicit_operator', 'da2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/quotes_apostrophes',
                component: ComponentCreator('/docs/howdo/contents/what_dif/quotes_apostrophes', '25e'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/set_let',
                component: ComponentCreator('/docs/howdo/contents/what_dif/set_let', '15b'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/contents/what_dif/subexpression',
                component: ComponentCreator('/docs/howdo/contents/what_dif/subexpression', 'ee2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/history',
                component: ComponentCreator('/docs/howdo/history', 'e24'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/intro',
                component: ComponentCreator('/docs/howdo/intro', '667'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/links',
                component: ComponentCreator('/docs/howdo/links', '196'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/qsp_keywords/qsp-keyword-functions',
                component: ComponentCreator('/docs/howdo/qsp_keywords/qsp-keyword-functions', '7d2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/qsp_keywords/qsp-keyword-operacion',
                component: ComponentCreator('/docs/howdo/qsp_keywords/qsp-keyword-operacion', '88d'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/qsp_keywords/qsp-keyword-operators',
                component: ComponentCreator('/docs/howdo/qsp_keywords/qsp-keyword-operators', 'fb2'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/qsp_keywords/qsp-keyword-pointer',
                component: ComponentCreator('/docs/howdo/qsp_keywords/qsp-keyword-pointer', '1b1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/qsp_keywords/qsp-keyword-syntaxems',
                component: ComponentCreator('/docs/howdo/qsp_keywords/qsp-keyword-syntaxems', 'e58'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/howdo/qsp_keywords/qsp-keyword-sys-var',
                component: ComponentCreator('/docs/howdo/qsp_keywords/qsp-keyword-sys-var', '3c1'),
                exact: true,
                sidebar: "howdoSidebar"
              },
              {
                path: '/docs/informarch/aeroqsp/aeroqsp_help',
                component: ComponentCreator('/docs/informarch/aeroqsp/aeroqsp_help', 'd1d'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/aeroqsp/aeroqsp_instr',
                component: ComponentCreator('/docs/informarch/aeroqsp/aeroqsp_instr', '559'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/aeroqsp/guidebook',
                component: ComponentCreator('/docs/informarch/aeroqsp/guidebook', '211'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/aeroqsp/not_work_attrib',
                component: ComponentCreator('/docs/informarch/aeroqsp/not_work_attrib', '9ff'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/aeroqsp/not_work_hyperlink',
                component: ComponentCreator('/docs/informarch/aeroqsp/not_work_hyperlink', '95c'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/aeroqsp/standalone_aeroqsp',
                component: ComponentCreator('/docs/informarch/aeroqsp/standalone_aeroqsp', 'b7c'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/aeroqsp/wit/',
                component: ComponentCreator('/docs/informarch/aeroqsp/wit/', '247'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/bookmarks',
                component: ComponentCreator('/docs/informarch/bookmarks', '604'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/extrqsp/automat_programming/',
                component: ComponentCreator('/docs/informarch/extrqsp/automat_programming/', '6d6'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/extrqsp/console_player',
                component: ComponentCreator('/docs/informarch/extrqsp/console_player', '327'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/general/code_analyser',
                component: ComponentCreator('/docs/informarch/general/code_analyser', 'dd8'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/general/game_shelf',
                component: ComponentCreator('/docs/informarch/general/game_shelf', '0c3'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/general/localization_classic_570',
                component: ComponentCreator('/docs/informarch/general/localization_classic_570', '459'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/general/qgen_dev_guide/',
                component: ComponentCreator('/docs/informarch/general/qgen_dev_guide/', '031'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/general/standalone_classic',
                component: ComponentCreator('/docs/informarch/general/standalone_classic', 'c80'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/intro',
                component: ComponentCreator('/docs/informarch/intro', 'a49'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/add_user_font',
                component: ComponentCreator('/docs/informarch/navigator/add_user_font', '6d4'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/change_background_color',
                component: ComponentCreator('/docs/informarch/navigator/change_background_color', 'ce7'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/change_cursor',
                component: ComponentCreator('/docs/informarch/navigator/change_cursor', '322'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/change_interface',
                component: ComponentCreator('/docs/informarch/navigator/change_interface', '484'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/exec_js',
                component: ComponentCreator('/docs/informarch/navigator/exec_js', '51d'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/externallinks',
                component: ComponentCreator('/docs/informarch/navigator/externallinks', '3a6'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/layout_templates',
                component: ComponentCreator('/docs/informarch/navigator/layout_templates', '026'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/modal_window',
                component: ComponentCreator('/docs/informarch/navigator/modal_window', '4ca'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/proverka_pleera',
                component: ComponentCreator('/docs/informarch/navigator/proverka_pleera', 'd4e'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/standalone',
                component: ComponentCreator('/docs/informarch/navigator/standalone', '6b9'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/template_settings',
                component: ComponentCreator('/docs/informarch/navigator/template_settings', 'e96'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/video',
                component: ComponentCreator('/docs/informarch/navigator/video', '7a1'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/navigator/windows_size',
                component: ComponentCreator('/docs/informarch/navigator/windows_size', '4e4'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/choose_card_in_deck',
                component: ComponentCreator('/docs/informarch/program/choose_card_in_deck', '360'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/conditional_actions',
                component: ComponentCreator('/docs/informarch/program/conditional_actions', '424'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/debugger_200beta',
                component: ComponentCreator('/docs/informarch/program/debugger_200beta', 'a82'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/game_time',
                component: ComponentCreator('/docs/informarch/program/game_time', 'b9b'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/julian_calendar',
                component: ComponentCreator('/docs/informarch/program/julian_calendar', 'e87'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/lib_extend_inventory',
                component: ComponentCreator('/docs/informarch/program/lib_extend_inventory', '1ee'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/lib_flex_playlist',
                component: ComponentCreator('/docs/informarch/program/lib_flex_playlist', '4f1'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/smooth_background',
                component: ComponentCreator('/docs/informarch/program/smooth_background', 'a5b'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/program/use_arrays',
                component: ComponentCreator('/docs/informarch/program/use_arrays', '4e6'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/qspider/deleting_games',
                component: ComponentCreator('/docs/informarch/qspider/deleting_games', '0c1'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/review/compo_2010',
                component: ComponentCreator('/docs/informarch/review/compo_2010', '57a'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/txtgam/preprocessor',
                component: ComponentCreator('/docs/informarch/txtgam/preprocessor', '399'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/txtgam/text_editor',
                component: ComponentCreator('/docs/informarch/txtgam/text_editor', '767'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/txtgam/txt2gam_for_linux',
                component: ComponentCreator('/docs/informarch/txtgam/txt2gam_for_linux', 'a13'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/txtgam/txt2gam_help',
                component: ComponentCreator('/docs/informarch/txtgam/txt2gam_help', '5a6'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/updates/classic_to_570',
                component: ComponentCreator('/docs/informarch/updates/classic_to_570', 'aa9'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/wii_qsp/info',
                component: ComponentCreator('/docs/informarch/wii_qsp/info', 'f2f'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/wii_qsp/our_way',
                component: ComponentCreator('/docs/informarch/wii_qsp/our_way', 'cc4'),
                exact: true,
                sidebar: "informArchSidebar"
              },
              {
                path: '/docs/informarch/wii_qsp/short_faq',
                component: ComponentCreator('/docs/informarch/wii_qsp/short_faq', '354'),
                exact: true,
                sidebar: "informArchSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', 'e5f'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
