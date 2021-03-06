Managing Lessons for Learn.KnightLab.com
----------------------------------------

This CMS is a work in progress. Please be patient, and if things are awkward or confusing, perhaps it's an opportunity to better understand how all these parts fit together.

As of today, the CMS supports creating the following content types:
* Lesson
* Zooming Image
* Capsule units

For a little while, we'll use this document to keep track of things to know. We can also add some notes directly in the admin user interface and welcome your suggestions about how to make that better.

## Lessons

* Title: hopefully obvious
* Slug: don't edit this
* Banner image: upload an appropriate file. We should establish image size guidelines, and if possible, enforce them in the authoring tool
* Status: experimental. For now, 'draft' is only visible by logged in users.
* Reference blurb: this is the part that gets shown if this lesson is referenced from another
* Content: this is the biggie

Note that there's a button in the top right corner, "View on site >", which you can use to see your work. It's not a "preview," so you have to save first. (Probably "Save and continue editing" in most cases.)

### More on Lesson Content

The first thing should be the `<narrative-text>` element. Everything you're used to seeing above that is handled by other tools.

Otherwise, for now mostly follow the examples you've been working from. A few more notes:

**Make the text field bigger** -
We're looking at ways to improve the presentation, but for now, don't forget that most browsers let you resize `textarea` fields, so be good to yourself and make the *Content* field real big before you do much more.

**narrative-text** -
Not much to know. Based on the original design, this is at the top of each lesson. Contents can be any HTML

**info-block** -
These no longer take an `image` attribute. Content can be any HTML markup.

**code-block** -
These are preformatted text, so don't indent the contents to match their container. You can indent lines within the block if you like.

**link-ref** -
We need to figure out the right way to handle images for these. It would help to know if we want to think of these as shared between lessons or capsule units or if we just want them to be one-offs. Let's talk after we get comfortable with the basics.


#### References
Zooming images, lesson references, and capsule units have special behavior so you don't copy their content over and over again. For each of these, the way to include that content is with a `ref` attribute. The value of the `ref` attribute should be the `slug` from the thing you want to load. At this time, invalid refs should be visible for logged in users, but will get stripped out from published docs (but we wouldn't want to publish those anyway, we would want to fix them.)  So for example:

    <lesson-ref ref="create-basic-website" ></lesson-ref>
    <capsule-unit ref="text-editor"></capsule-unit>
    <zooming-image ref="mac-file-system"></zooming-image>

As you can see, you leave out the other attributes -- those get filled in by the CMS.

## Zooming Images

For now, assign the `slug` yourself. Maybe we can make that more automatic, but I don't know for sure what's worthwhile.  Just upload the "full size" image; the smaller version gets made automatically.

## Capsule Units
The animations for these are a little wack, so they're hard to preview correctly. Should be fixed soon.

## Glossary Terms

There's now a model object for glossary terms. "Lemma" is a fancy lexicographer's word for the main word you use to define things, even though it might show up in alternate forms: e.g. "HTML" or "Hypertext Markup Language."

To mark a term as a glossary-term, just wrap it in &lt;glossary-term&gt; tags. Then go and create a matching term and definition in the admin tool. If you want to use something in text which isn't the exact "lemma", then you can use a "lemma" attribute to link to the right definition.  For now, posts in draft mode will show the definition as a link even if there isn't yet a matching term, but published posts will not let those be clickable.  Also, for now, the text inside the `glossary-term` tags must exactly match the lemma in the admin (including case). You can use the `lemma` attribute to assist. Doing case-insensitive matches could add overhead for pages with lots of terms, but we could do it if it makes sense.
