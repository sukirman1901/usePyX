from pyx import App, ui

app = App()

def onboarding():
    return ui.div(
        # --- 1. Background Layers ---
        # Soft Gradient Background
        ui.div(
            # Top-left gradient
            ui.div()\
                .absolute().top(0).left(0).w("700px").h("700px")\
                .style(background="linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(244, 63, 94, 0.1), transparent)")\
                .style(border_radius="9999px", filter="blur(60px)", transform="translate(-50%, -50%)")\
                .z(0),
            
            # Bottom-right gradient
            ui.div()\
                .absolute().bottom(0).right(0).w("500px").h("500px")\
                .style(background="linear-gradient(315deg, rgba(249, 115, 22, 0.15), rgba(239, 68, 68, 0.08), transparent)")\
                .style(border_radius="9999px", filter="blur(60px)", transform="translate(33%, 33%)")\
                .z(0)
        ).absolute().top(0).left(0).w_full().h_full().z(0),

        # --- 2. Content Container ---
        ui.div(
            # Main Content Grid
            ui.div(
                ui.div(
                    # --- Left Column: Documentation Card (Large) ---
                    ui.div(
                        ui.div(
                            # Browser Mockup inside card
                            ui.div(
                                ui.div(
                                    ui.div().w(2.5).h(2.5).rounded("full").bg("red-400"),
                                    ui.div().w(2.5).h(2.5).rounded("full").bg("yellow-400"),
                                    ui.div().w(2.5).h(2.5).rounded("full").bg("green-400"),
                                ).flex().gap(1.5),
                                ui.div("docs.pyx.framework")\
                                    .ml(3).flex_1().bg("white").rounded().px(3).py(1)\
                                    .text("xs").text("gray-400").border().border_color("gray-200")
                            ).flex().items("center").gap(2).mb(3),
                            
                            ui.div(
                                ui.div().h(2).bg("gray-200").rounded().w("1/4"),
                                ui.div().h(2).bg("gray-200").rounded().w("3/4"),
                                ui.div().h(2).bg("gray-200").rounded().w("2/3"),
                                ui.div().h(2.5).bg("red-500").rounded().w("1/3").mt(3),
                                ui.div(
                                    ui.div().h(1.5).bg("gray-200").rounded(),
                                    ui.div().h(1.5).bg("gray-200").rounded().w("5/6"),
                                    ui.div().h(1.5).bg("gray-200").rounded().w("4/5"),
                                ).space_y(2).mt(3)
                            ).space_y(2.5)
                        ).mb(6).bg("gray-50").rounded("lg").p(5).border().border_color("gray-200"),

                        # Icon
                        ui.div(
                            ui.i(data_lucide="book-open").w(6).h(6).text("red-500")
                        ).w(12).h(12).rounded("lg").bg("red-50").flex().items("center").justify("center").mb(5),

                        # Text Content
                        ui.h2("Documentation").text("2xl").font("bold").text("gray-900").mb(3),
                        ui.p("PyX has wonderful documentation covering every aspect of the framework. Whether you are a newcomer or have prior experience with PyX, we recommend reading our documentation from beginning to end.")\
                            .text("gray-600").leading("relaxed").mb(5).flex_1().text("sm"),

                        # CTA Link
                        ui.a(
                            "Read Documentation",
                            ui.i(data_lucide="arrow-right").w(4).h(4).ml(2)
                        ).inline_flex().items("center").text("red-500").font("semibold").text("sm")\
                         .hover("text-red-600").hover("gap-3").transition("all").cursor("pointer").no_underline(),

                    ).bg("white/70").backdrop_blur("sm").rounded("xl").p(8).shadow("sm").border().border_color("gray-100")\
                     .h_full().flex().flex_col().group().hover("shadow-md").transition("shadow").duration(300).cls("lg:row-span-2"),

                    # --- Right Column ---
                    
                    # Card 2: PyX Framework
                    ui.div(
                        ui.div(
                            ui.div(
                                ui.i(data_lucide="sparkles").w(6).h(6).text("red-500")
                            ).w(12).h(12).rounded("lg").bg("red-50").flex().items("center").justify("center").shrink_0(),
                            
                            ui.div(
                                ui.h3("PyX Framework").text("xl").font("bold").text("gray-900").mb(2),
                                ui.p("PyX empowers you to build modern, reactive web applications entirely in Python. Forget about complex JavaScript build tools and context switching. Just write Python, and let PyX handle the rest.")\
                                    .text("gray-600").leading("relaxed").mb(3).text("sm"),
                                ui.a(
                                    ui.i(data_lucide="arrow-right").w(4).h(4)
                                ).inline_flex().items("center").text("red-500").font("semibold").text("sm")\
                                 .group_hover("translate-x-1").transition("transform").cursor("pointer")
                            ).flex_1()
                        ).flex().items("start").gap(5)
                    ).bg("white/70").backdrop_blur("sm").rounded("xl").p(6).shadow("sm").border().border_color("gray-100")\
                     .group().hover("shadow-md").transition("shadow").duration(300),

                    # Card 3: Batteries Included
                    ui.div(
                        ui.div(
                            ui.div(
                                ui.i(data_lucide="layers").w(6).h(6).text("red-500")
                            ).w(12).h(12).rounded("lg").bg("red-50").flex().items("center").justify("center").shrink_0(),
                            
                            ui.div(
                                ui.h3("Batteries Included").text("xl").font("bold").text("gray-900").mb(2),
                                ui.p("PyX ships with everything you need: Authentication, Database ORM, Real-time WebSockets, Background Jobs, and more. No need to glue together dozens of libraries.")\
                                    .text("gray-600").leading("relaxed").mb(3).text("sm"),
                                ui.a(
                                    ui.i(data_lucide="arrow-right").w(4).h(4)
                                ).inline_flex().items("center").text("red-500").font("semibold").text("sm")\
                                 .group_hover("translate-x-1").transition("transform").cursor("pointer")
                            ).flex_1()
                        ).flex().items("start").gap(5)
                    ).bg("white/70").backdrop_blur("sm").rounded("xl").p(6).shadow("sm").border().border_color("gray-100")\
                     .group().hover("shadow-md").transition("shadow").duration(300),

                ).grid().cols(1).lg("grid-cols-2").gap(6)
            ).max_w("6xl").mx("auto").px(6).pb(6),
            
            # AI & Cloud Native
            ui.div(
                ui.div(
                    # Card 4: AI & Cloud Native
                    ui.div(
                        ui.div(
                            ui.div(
                                ui.i(data_lucide="cpu").w(6).h(6).text("red-500")
                            ).w(12).h(12).rounded("lg").bg("red-50").flex().items("center").justify("center").shrink_0(),
                            
                            ui.div(
                                ui.h3("AI & Cloud Native").text("xl").font("bold").text("gray-900").mb(2),
                                ui.p("Built for the future with first-class support for AI LLM integration and unified Cloud Storage (S3/GCS). Deploy anywhere with our Rust-powered engine for maximum performance.")\
                                    .text("gray-600").leading("relaxed").mb(3).text("sm"),
                                ui.a(
                                    ui.i(data_lucide="arrow-right").w(4).h(4)
                                ).inline_flex().items("center").text("red-500").font("semibold").text("sm")\
                                 .group_hover("translate-x-1").transition("transform").cursor("pointer")
                            ).flex_1()
                        ).flex().items("start").gap(5)
                    ).bg("white/70").backdrop_blur("sm").rounded("xl").p(6).shadow("sm").border().border_color("gray-100")\
                     .group().hover("shadow-md").transition("shadow").duration(300),

                ).grid().cols(1)
            ).max_w("6xl").mx("auto").px(6).pb(16),
           
            # Footer
            ui.div("PyX v0.1.0 (Python v3.11)").text_align("center").pb(8).text("xs").text("gray-500")

        ).relative().z(10).w_full()

    ).min_h("100vh").bg("white").relative().overflow("hidden").font("Inter").pt(40)

app.add_page("/", onboarding)

if __name__ == "__main__":
    app.run(port=8083)