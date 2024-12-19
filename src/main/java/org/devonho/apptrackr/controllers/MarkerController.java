package org.devonho.apptrackr.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MarkerController {
    @RequestMapping(value="/map")
    public String trafficSpy() {
        return "index";
    }
} 