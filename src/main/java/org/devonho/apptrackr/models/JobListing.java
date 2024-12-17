package org.devonho.apptrackr.models;

import java.util.Date;

import org.springframework.data.annotation.Id;

public class JobListing {
    
	final private String jobTitle;
	final private String jobListingURL;
    final private String jobListingDescription;
    final private Date jobListingDate;

    public JobListing(String jobTitle, String jobListingURL, String jobListingDescription, Date jobListingDate) {
        this.jobTitle = jobTitle;
        this.jobListingURL = jobListingURL;
        this.jobListingDescription = jobListingDescription;
        this.jobListingDate = jobListingDate;
    }

	public String getJobTitle() {
		return jobTitle;
	}

	public String getJobListingURL() {
		return jobListingURL;
	}

    public String getJobListingDescription() {
        return jobListingDescription;
    }

    public Date getJobListingDate() {
        return jobListingDate;
    }

}
