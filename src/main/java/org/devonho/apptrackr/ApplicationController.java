package org.devonho.apptrackr;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ApplicationController {

  	@Autowired
  	private ApplicationRepository repository;

    @PostMapping("/application")
    public static String createApplication(@RequestBody Application application) {
        return "OK";
    }
}
