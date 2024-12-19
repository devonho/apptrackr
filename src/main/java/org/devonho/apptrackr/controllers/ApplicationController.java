package org.devonho.apptrackr.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.QueryDocumentSnapshot;
import com.google.cloud.firestore.QuerySnapshot;

import org.devonho.apptrackr.models.Application;
import org.devonho.apptrackr.models.JobListing;

@RequestMapping("application")
@RestController
public class ApplicationController {

    private Logger logger = LoggerFactory.getLogger(Logger.class);

    @Autowired
    private Firestore db;

    @PostMapping()
    public void createApplication(@RequestBody Application application) {
      try {
        DocumentReference docRef = db.collection("applications").document(application.getId());
        docRef.set(application);
      } catch (Exception e) {
        logger.error(e.getMessage());
      }
    }

    @GetMapping()
    public Application getApplicationById(String id) {
      try {
        ApiFuture<QuerySnapshot> querySnapshot = db.collection("applications").whereEqualTo("id", id).get();

        QueryDocumentSnapshot document = querySnapshot.get().getDocuments().get(0);

        JobListing listing = new JobListing();
        listing.setJobTitle(document.getString("jobListing.jobTitle"));
        listing.setJobListingDescription(document.getString("jobListing.jobListingDescription"));
        listing.setJobListingURL(document.getString("jobListing.jobListingURL"));
        listing.setJobListingDate(document.getDate("jobListing.jobListingDate"));

        Application app = new Application();
        app.setId(document.getId());
        app.setJobListing(listing);
        
        return app;        
      } catch (Exception e) {
        logger.error(e.getMessage());
        return null;
      }      
    }
   
}
