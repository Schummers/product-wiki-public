---
title: "Listboxes vs. Dropdown Lists"
date: "2020-04-12"
url: "https://www.nngroup.com/articles/listbox-dropdown/"
author: "Anna Kaley"
topics: [applications, interaction-design, web-usability]
type: article
---

Many UI controls allow users to select options; they include [checkboxes](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/), [radio buttons](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/), [toggle switches](https://www.nngroup.com/articles/toggle-switch-guidelines/), [steppers](https://www.nngroup.com/articles/input-steppers/), listboxes, and [dropdowns](https://www.nngroup.com/articles/drop-down-menus/). In this article, I’ll define listboxes and dropdown lists, discuss when to use each element, and cases where either will suffice.

## In This Article:

- [Listboxes](#toc-listboxes-1)
- [Dropdown Lists](#toc-dropdown-lists-2)
- [Listboxes and Dropdown Lists in Use](#toc-listboxes-and-dropdown-lists-in-use-3)
- [Listbox Advantages and Disadvantages](#toc-listbox-advantages-and-disadvantages-4)
- [Dropdown-List Advantages and Disadvantages](#toc-dropdown-list-advantages-and-disadvantages-5)
- [Choosing Between a Listbox and a Dropdown List](#toc-choosing-between-a-listbox-and-a-dropdown-list-6)
- [Conclusion](#toc-conclusion-7)

## Listboxes

In their simplest form, a listbox contains three main parts: a **container box**, a **list of items**, and a **label**. Users can click on the items enclosed in the container box to select one or many from the list. A listbox may scroll, depending on how many items it contains and the viewable area. Sometimes, listboxes include checkboxes to clearly imply that multiselect functionality is available. More complex listboxes allow users to resize the container box, reorder the list of items, and make selections by moving items from one listbox to another.

There are 4 variations of listboxes that can be classified according to selection type. Each of these listboxes can be scrollable or not.

- **Single-select listbox:** With this type of listbox, users can select only one item from a list of mutually exclusive options.
- **Multiselect listbox:** Users can select or deselect one or more items by holding down the *Shift*, *Command*, or *Control* key while clicking on items.
- **Multiselect listbox with checkboxes:** This type of listbox includes checkboxes to make multiple selection more obvious.
- **Multiselect, dual listboxes:** This type of listbox consists of two listboxes. The listbox on the left holds available options and the listbox on the right represents selected items. The *Add* button moves an item from the available list to the selected list and the *Remove* button moves a selected option back to available list, to deselect it. Users can also move options up and down to reorder elements in the list.

![Classification of listboxes by scrollability and selection-type.](https://media.nngroup.com/media/editor/2020/03/05/1-final-listbox-matrix)

*Listboxes can remain static or scroll to reveal more items than their initial height exposes. They also support single-item or multi-item selection.*

![Multiselect dual listbox example](https://media.nngroup.com/media/editor/2020/03/05/2-multiselect-dual-listbox-final)

*A multiselect, dual listbox allows users to make selections by moving items from one listbox to another. Users can also reorder the options by moving them up and down in the list.*

## Dropdown Lists

In their simplest form, dropdown lists contain four main parts: a **container box**, a **downward-facing arrow button**, a **list of items**, and a **label**. Users can click on the down-arrow to display a list of mutually-exclusive items from which they can select only one. Like listboxes, dropdowns may scroll depending on how many items they contain when expanded. With dropdown lists, the selected option or default value remains visible in the container box, while the other list items appear only after clicking on the down-arrow. Selecting an item or clicking outside of the dropdown list will close it.

![Evolution of a dropdown from closed, to static, to scrollable.](https://media.nngroup.com/media/editor/2020/03/05/3-final-sidebyside-dropdowns)

*Dropdown lists display a single default or selected value enclosed in a container box. On click of the down-arrow button, a list of options appears from which users can select only one. A dropdown list can remain static or scroll depending on how many items it contains.*

![Evolution of a dropdown from closed, to static, to scrollable.](https://media.nngroup.com/media/editor/2020/03/05/4-mobile-stacked-dropdowns)

*Dropdown lists display a single default or selected value enclosed in a container box. On click of the down-arrow button, a list of options appears from which users can select only one. A dropdown list can remain static or scroll depending on how many items it contains.*

![Dropdowns classified by whether they're static or scrollable.](https://media.nngroup.com/media/editor/2020/03/05/5-final-dropdown-matrix)

*Dropdown lists do not support multiselect functionality; users can only select one option from either a static or scrollable list.*

## Listboxes and Dropdown Lists in Use

Listboxes and dropdown lists make a form compact — especially when many options are available, and presenting those options as a list of standalone radio buttons or checkboxes would take up an unnecessary amount of screen space. Using a listbox or a dropdown list can also [reduce errors](https://www.nngroup.com/articles/error-message-guidelines/) by constraining the options to those in the list and ensuring that users enter data in the proper format.

![Comparison of the space taken up between a list of radio buttons, a listbox, and a dropdown.](https://media.nngroup.com/media/editor/2020/03/05/6-final-compare-radiobuttons-listbox-dropdown)

*Lists of standalone radio buttons for single selection are appropriate when there is a small number of options available. With many options, use either a listbox or a dropdown list, depending on the screen space available and on how much you want to encourage users to make changes. Both elements hold more items and take up less screen space than listing many items vertically on the page.*

![Stacked height comparison of radio buttons, a listbox, and a dropdown.](https://media.nngroup.com/media/editor/2020/03/05/7-final-mobile-comparison-radiobutton-listbox-dropdown)

*Lists of standalone radio buttons for single selection are appropriate when there is a small number of options available. With many options, use either a listbox or a dropdown list, depending on the screen space available and on how much you want to encourage users to make changes. Both elements hold more items and take up less screen space than listing many items vertically on the page.*

![Height comparison of a list of checkboxes vs. a listbox](https://media.nngroup.com/media/editor/2020/03/05/8-final-checkbox-listbox)

*Lists of standalone checkboxes are appropriate to use for multiselection when there is a small number of options available. When many options are available, use a listbox as they hold  more items and take up less space than listing many checkboxes vertically on the page.*

Listboxes and dropdown lists are used for selection in both native applications and websites. They aren’t intended to execute commands or trigger the display of modal windows, dialog boxes, or dynamic controls. On ecommerce sites, listboxes are often used to house filters that cascade down the left side of a category page, while a dropdown list may house the values by which a user can sort the products.

![Example of how Sephora uses listboxes for their filters and a dropdown to sort products.](https://media.nngroup.com/media/editor/2020/03/05/sephoraexample-listboxes-dropdown-lists.jpg)

*Sephora.com uses scrollable, multiselect listboxes (left side) with checkboxes to house the filters on their shopping pages. Users can select one or many refinements from each listbox to narrow the set of products displayed. Sephora also uses a dropdown list (upper right) containing mutually exclusive values from which users can select to sort the page by a specific attribute.*

For scrollable listboxes and dropdown lists, it’s important to consider their size as it relates to the [Steering Law](https://www.nngroup.com/articles/steering-law/). The Steering Law predicts how long it will take a user to move a cursor or a finger through a bounded area known as a tunnel. The steering time depends on the length and the width of the tunnel, where shorter, wider tunnels are faster and easier for users to navigate through than longer, narrower tunnels. Thereby, limiting the number of items contained in scrollable listboxes and dropdowns, and ensuring they’re designed to be as wide and as short as possible will help users review and navigate with speed and ease. When dropdown lists grow too long and narrow, the user is more likely to accidentally move their cursor outside of the bounded area, which will close the dropdown and force them to start the selection process all over again.

## Listbox Advantages and Disadvantages

Though relatively seldom used, listboxes carry advantages beyond supporting single selection, multiselection, and housing many options without taking up excessive screen space. Other advantages of listboxes include:

- **Low interaction cost :** Listboxes don’t require users to click on anything to reveal the options inside before making a selection (but they may require users to scroll the list if there are too many items).
- **Increased item visibility:** The ability to see multiple options at once can speed up decision making and increase selection accuracy.
- **Single and multicolumn views:** because listboxes aren’t limited to a single column, more options can be made visible if the listbox width allows. However, horizontal scrolling should be avoided in multicolumn listboxes.
- **Overview and reordering:** with multiselect, dual listboxes, users maintain some control over the order in which items are displayed and get a clear overview of the items selected, which is helpful when the listbox contains several options.

Here are some disadvantages of listboxes:

- **Screen space:** Even though they’re compact, they do tend to take up more screen space than dropdown lists.
- **Unfamiliarity:** Users may not know how to interact with listboxes right away — specifically, they may not know how to choose multiples if checkboxes are not included in multiselect listboxes. Holding down the *Control*, *Command*, or *Shift* key to select and deselect multiple items is not something general web users do often. That’s why it’s important to include checkboxes in multiselect listboxes, unless they focus unwanted attention on multiselect functionality or add unnecessary screen clutter.
- **Users may not be able to see all of the selected options at once:** If there are many more items available beyond what’s visible in the viewable area, users may lose the ability to see all selected items simultaneously. To avoid this drawback, show selected items above the listbox as tokens or highlight the selected items in a nonscrollable list.​

## Dropdown-List Advantages and Disadvantages

Dropdown lists are used more frequently than listboxes; they take up less screen space but can hold just as many items as listboxes. Other advantages of dropdown lists include:

- **The ability to give users an optimal option,** selected by default.
- **Downplaying alternative options and changes:** Because dropdown lists hide the other available options, they work well to downplay alternatives and underemphasize the ability to make changes. (This is advantageous in cases where the default will satisfy most users and where the alternative options may be dangerous or confusing to nonexpert users.)
- **Familiarity:** Dropdown lists are familiar selection mechanisms for most users since they are widely used both on the web and in native apps.

A disadvantage of dropdown lists are that they require a click to reveal the options inside. Other disadvantages of dropdown lists include:

- **They’re subject to overstuffing** and can be cumbersome to scroll through when they contain too many options.
- **They slow users down** when they’re used to capture readily known values. For example, when entering a birthdate or credit-card expiration date, typing in a form field is usually faster and easier than interacting with dropdown lists.
- **Discreet:** Because they are so compact, users may accidentally overlook dropdown lists in forms, web pages, and applications.
- **Easy to dismiss:** Accidentally deviating the cursor from the box closes the dropdown and people have to start the selection process all over again.

## Choosing Between a Listbox and a Dropdown List

Compared to using standalone checkboxes or radio buttons, it’s better to use a listbox or dropdown list when there are 5 or more items from which users can choose. Additional factors such as the amount of screen space available, whether the user can select one or many items, and if there’s a need to downplay or encourage changes all need to be considered when deciding between a listbox, a dropdown list, or another selection control. Use the criteria in the table below to help you decide which element to use or when either will suffice.

Criteria to Consider | Use a Dropdown List | Use a Listbox | Either is Acceptable | When to Use Another Control | The list of options is comprised of objects (nouns) or attributes (adjectives). | ✓ | ✓ | ✓ | Use a button to trigger commands (verbs). | There’s a small number of options (5 or fewer) from which users can choose. | X | X | X | Use radio buttons for small sets of mutually exclusive items or checkboxes for multiselect items. | There are 5–15 options. | ✓ | ✓ | Use a dropdown if screen space is limited. Use a listbox if it is not. | X | There are more than 15 options. | X | Make all or most of the options initially visible in the listbox. Don’t use a listbox if it forces users to scroll excessively. | X | If screen space is limited and users are likely to know the exact value, let them type it in a form field. | Users can select only one value from a list of mutually exclusive options. | ✓ | ✓ | Use a dropdown if there’s limited screen space, an optimal default value, and to downplay alternatives and  making changes. Use a single-select listbox if screen space is available, to draw more attention to the options, and to encourage changes. | For small sets of options, use radio buttons. | Users can select one or many from the list of options. | X | Use a multiselect listbox with checkboxes to imply multiple selection. | X | For small sets of options, use standalone checkboxes. | Seeing the selected item is more important than viewing the other available options. | ✓ | X | X | X | Seeing an overview of all items, selected or not, aids in task completion. | X | ✓ | X | X | There’s not a clear or optimal default option. | X | ✓ | X | X | The order in which options are ranked is an important factor in selection. | X | Use a multiselect, dual listbox to accommodate both selection and reordering. | X | X

Criteria to Consider | What to Do | The list of options is comprised of objects (nouns) or attributes (adjectives) | . | In this case, it's acceptable to use either a listbox or a dropdown list. Use a button to trigger commands (verbs). | There’s a small number of options (5 or fewer) from which users can choose. | Do not use a listbox or a dropdown list; use radio buttons for small sets of mutually exclusive items or checkboxes for multiselect items. | There are 5–15 options. | It's acceptable to use either a listbox or a dropdown list. Favor a dropdown list if screen space is limited. Use a listbox if it is not. | There are more than 15 options. | Use a listbox and make all or most of the options initially visible. Don’t use a listbox if it forces users to scroll excessively. If screen space is limited and users are likely to know the exact value, let them type it in a form field. | Users can select only one value from a list of mutually exclusive options. | It's acceptable to use either a listbox or a dropdown list. Use a dropdown if there’s limited screen space, an optimal default value, and to downplay alternatives and making changes. Use a single-select listbox if screen space is available, to draw more attention to the options, and to encourage changes. For small sets of options, use radio buttons. | Users can select one or many from the list of options. | Do not use a dropdown list. Use a multiselect listbox with checkboxes to imply multiple selection. For small sets of options, use standalone checkboxes. | Seeing the selected item is more important than viewing the other available options. | Use a dropdown list. | Seeing an overview of all items, selected or not, aids in task completion. | Use a listbox. | There’s not a clear or optimal default option. | Use a listbox. | The order in which options are ranked is an important factor in selection. | Use a multiselect, dual listbox to accommodate both selection and reordering.

## Conclusion

When including a listbox or dropdown list in your design, always display the options in a logical order. That may mean [grouping related items together](https://www.nngroup.com/articles/form-design-white-space/), placing the most commonly selected item first, or organizing the options in alphabetical order. Always place numbers and dates in sequential order.
